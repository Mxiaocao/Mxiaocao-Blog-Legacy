#!/usr/bin/env python3
"""
Recover Hexo-generated article HTML from Mxiaocao-Blog-Legacy into
Astro/Mizuki-friendly Markdown.

The legacy repository contains the generated static site rather than the
original source/_posts Markdown. This script intentionally favors
preservation over prettiness: normal HTML becomes Markdown, code blocks are
reconstructed as fenced code, surviving TeX is restored, and already-rendered
MathJax SVG is preserved as raw HTML instead of being silently discarded.
"""

from __future__ import annotations

import html as html_lib
import json
import re
from collections import Counter
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit

from bs4 import BeautifulSoup, NavigableString
from markdownify import markdownify as html_to_markdown

ROOT = Path(__file__).resolve().parents[1]
SOURCE_ROOT = ROOT / "2026"
OUT_ROOT = ROOT / "recovered-mizuki"
POSTS_ROOT = OUT_ROOT / "src" / "content" / "posts"
REPORT_PATH = OUT_ROOT / "recovery-report.json"
ASSET_MANIFEST_PATH = OUT_ROOT / "asset-manifest.txt"
README_PATH = OUT_ROOT / "README.md"

OLD_HOSTS = {
    "mxiaocaoblog.com",
    "www.mxiaocaoblog.com",
}

EXPECTED_POST_COUNT = 41


def yaml_string(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def normalize_whitespace(value: str) -> str:
    return re.sub(r"\s+", " ", html_lib.unescape(value or "")).strip()


def date_only(value: str | None) -> str | None:
    if not value:
        return None
    match = re.match(r"(\d{4}-\d{2}-\d{2})", value)
    return match.group(1) if match else value


def normalize_url(url: str | None, asset_paths: set[str]) -> str | None:
    if not url:
        return url

    url = html_lib.unescape(url.strip())
    parsed = urlsplit(url)

    if parsed.scheme in {"http", "https"} and parsed.netloc.lower() in OLD_HOSTS:
        parsed = parsed._replace(scheme="", netloc="")
        url = urlunsplit(parsed)
    elif parsed.scheme or parsed.netloc:
        return url

    parsed = urlsplit(url)
    path = parsed.path

    if path.startswith("/img/"):
        asset_paths.add(path.lstrip("/"))

    match = re.match(
        r"^/2026/\d{2}/\d{2}/([^/]+?)/(?:index\.html)?$",
        path,
        flags=re.IGNORECASE,
    )
    if match:
        path = f"/posts/{match.group(1)}/"
        parsed = parsed._replace(path=path)
        return urlunsplit(parsed)

    match = re.match(
        r"^/2026/\d{2}/\d{2}/([^/]+?)(?:/index\.html)?$",
        path,
        flags=re.IGNORECASE,
    )
    if match and "." not in match.group(1):
        path = f"/posts/{match.group(1)}/"
        parsed = parsed._replace(path=path)
        return urlunsplit(parsed)

    return url


def make_placeholder(
    node,
    replacement: str,
    placeholders: dict[str, str],
    counter: list[int],
) -> None:
    token = f"RECOVERYPLACEHOLDER{counter[0]:06d}TOKEN"
    counter[0] += 1
    placeholders[token] = replacement
    node.replace_with(NavigableString(token))


def recover_code_blocks(
    article,
    placeholders: dict[str, str],
    counter: list[int],
) -> int:
    count = 0
    fence = chr(96) * 3
    for figure in list(article.select("figure.highlight")):
        classes = figure.get("class", [])
        language = next((c for c in classes if c != "highlight"), "")
        language = {
            "c++": "cpp",
            "cxx": "cpp",
            "js": "javascript",
            "sh": "bash",
        }.get(language.lower(), language)

        code_pre = figure.select_one("td.code pre") or figure.find("pre")
        if code_pre is None:
            continue

        line_nodes = code_pre.select("span.line")
        if line_nodes:
            code = "\n".join(
                line.get_text("", strip=False) for line in line_nodes
            )
        else:
            code_soup = BeautifulSoup(str(code_pre), "html.parser")
            for br in code_soup.find_all("br"):
                br.replace_with("\n")
            code = code_soup.get_text("", strip=False)

        code = html_lib.unescape(code).rstrip("\n")
        replacement = f"\n{fence}{language}\n{code}\n{fence}\n"
        make_placeholder(figure, replacement, placeholders, counter)
        count += 1

    return count


def protect_math_and_embeds(
    article,
    placeholders: dict[str, str],
    counter: list[int],
) -> tuple[int, int, int]:
    tex_count = 0
    mathjax_count = 0
    embed_count = 0

    for script in list(article.select('script[type^="math/tex"]')):
        tex = script.string if script.string is not None else script.get_text()
        tex = (tex or "").strip()
        is_display = "mode=display" in script.get("type", "")
        if is_display:
            replacement = "\n$$\n" + tex + "\n$$\n"
        else:
            replacement = "$" + tex + "$"
        make_placeholder(script, replacement, placeholders, counter)
        tex_count += 1

    for mjx in list(article.find_all("mjx-container")):
        is_display = str(mjx.get("display", "")).lower() == "true"
        raw = str(mjx)
        replacement = f"\n{raw}\n" if is_display else raw
        make_placeholder(mjx, replacement, placeholders, counter)
        mathjax_count += 1

    preserve_tags = ["iframe", "video", "audio", "details", "canvas"]
    for tag_name in preserve_tags:
        for node in list(article.find_all(tag_name)):
            make_placeholder(node, f"\n{str(node)}\n", placeholders, counter)
            embed_count += 1

    for svg in list(article.find_all("svg")):
        make_placeholder(svg, f"\n{str(svg)}\n", placeholders, counter)
        embed_count += 1

    return tex_count, mathjax_count, embed_count


def rewrite_article_urls(article, asset_paths: set[str]) -> None:
    for link in article.find_all("a", href=True):
        normalized = normalize_url(link.get("href"), asset_paths)
        if normalized:
            link["href"] = normalized

    for image in article.find_all("img"):
        lazy_src = (
            image.get("data-lazy-src")
            or image.get("data-src")
            or image.get("src")
        )
        if lazy_src:
            normalized = normalize_url(lazy_src, asset_paths)
            if normalized:
                image["src"] = normalized

        for attr in ("data-lazy-src", "data-src"):
            image.attrs.pop(attr, None)

    for media in article.find_all(["source", "video", "audio", "iframe"]):
        if media.get("src"):
            normalized = normalize_url(media.get("src"), asset_paths)
            if normalized:
                media["src"] = normalized


def clean_article(article) -> None:
    for node in list(article.select("#post-outdate-notice")):
        node.decompose()

    for heading in article.find_all(re.compile(r"^h[1-6]$")):
        for anchor in list(heading.select("a.headerlink")):
            anchor.decompose()

    for style in list(article.find_all("style")):
        style.decompose()
    for script in list(article.find_all("script")):
        if not str(script.get("type", "")).startswith("math/tex"):
            script.decompose()


def extract_post(path: Path, all_asset_paths: set[str]) -> dict:
    raw_html = path.read_text(encoding="utf-8")
    soup = BeautifulSoup(raw_html, "html.parser")

    article = soup.select_one("#article-container")
    if article is None:
        raise RuntimeError(f"Missing #article-container in {path}")

    title_meta = soup.find("meta", property="og:title")
    title_node = soup.select_one("h1.post-title")
    title = (
        title_meta.get("content")
        if title_meta and title_meta.get("content")
        else (title_node.get_text(strip=True) if title_node else path.parent.name)
    )

    published_meta = soup.find("meta", property="article:published_time")
    updated_meta = soup.find("meta", property="article:modified_time")
    published = date_only(published_meta.get("content") if published_meta else None)
    updated = date_only(updated_meta.get("content") if updated_meta else None)

    description_meta = soup.find("meta", attrs={"name": "description"})
    description = normalize_whitespace(
        description_meta.get("content", "") if description_meta else ""
    )
    if len(description) > 220:
        description = description[:217].rstrip() + "..."

    image_meta = soup.find("meta", property="og:image")
    image = normalize_url(
        image_meta.get("content") if image_meta else None,
        all_asset_paths,
    )

    tags = []
    for meta in soup.find_all("meta", property="article:tag"):
        tag = normalize_whitespace(meta.get("content", ""))
        if tag and tag not in tags:
            tags.append(tag)

    category_node = soup.select_one("a.post-meta-categories")
    category = (
        normalize_whitespace(category_node.get_text(" ", strip=True))
        if category_node
        else ""
    )

    canonical = soup.find("link", rel="canonical")
    source_link = (
        canonical.get("href")
        if canonical and canonical.get("href")
        else f"https://www.mxiaocaoblog.com/2026/{path.relative_to(SOURCE_ROOT).parent.as_posix()}/"
    )

    article_asset_paths: set[str] = set()
    rewrite_article_urls(article, article_asset_paths)
    all_asset_paths.update(article_asset_paths)

    clean_article(article)

    placeholders: dict[str, str] = {}
    counter = [0]
    code_blocks = recover_code_blocks(article, placeholders, counter)
    tex_blocks, mathjax_svg_blocks, embed_blocks = protect_math_and_embeds(
        article, placeholders, counter
    )

    markdown = html_to_markdown(
        str(article),
        heading_style="ATX",
        bullets="-",
    )

    markdown = re.sub(r"[ \t]+\n", "\n", markdown)
    markdown = re.sub(r"\n{4,}", "\n\n\n", markdown).strip()

    for token, replacement in placeholders.items():
        markdown = markdown.replace(token, replacement)

    markdown = markdown.strip() + "\n"

    slug = path.parent.name
    output_path = POSTS_ROOT / f"{slug}.md"

    frontmatter = [
        "---",
        f"title: {yaml_string(normalize_whitespace(title))}",
        f"published: {published or '1970-01-01'}",
    ]
    if updated:
        frontmatter.append(f"updated: {updated}")
    if description:
        frontmatter.append(f"description: {yaml_string(description)}")
    if image:
        frontmatter.append(f"image: {yaml_string(image)}")
    frontmatter.append(
        "tags: [" + ", ".join(yaml_string(tag) for tag in tags) + "]"
    )
    if category:
        frontmatter.append(f"category: {yaml_string(category)}")
    frontmatter.extend(
        [
            "draft: false",
            "pinned: false",
            "comment: true",
            'author: "Mxiaocao"',
            f"sourceLink: {yaml_string(source_link)}",
            'licenseName: "CC BY-NC-SA 4.0"',
            "---",
            "",
        ]
    )

    output_path.write_text(
        "\n".join(frontmatter) + markdown,
        encoding="utf-8",
    )

    return {
        "source": path.relative_to(ROOT).as_posix(),
        "output": output_path.relative_to(ROOT).as_posix(),
        "slug": slug,
        "title": normalize_whitespace(title),
        "published": published,
        "updated": updated,
        "category": category or None,
        "tags": tags,
        "image": image,
        "sourceLink": source_link,
        "codeBlocksRecovered": code_blocks,
        "texBlocksRecovered": tex_blocks,
        "mathJaxSvgBlocksPreserved": mathjax_svg_blocks,
        "richEmbedsPreserved": embed_blocks,
        "localAssetsReferenced": sorted(article_asset_paths),
    }


def write_readme(report: dict) -> None:
    summary = report["summary"]
    readme = f"""# Legacy blog recovery for Astro + Mizuki

This directory is generated from the deployed Hexo HTML in the legacy
repository. The original source/_posts Markdown was not present, so the
recovery is an HTML-to-Markdown reconstruction.

## Recovered content

- Markdown posts: {summary["postsRecovered"]}
- Code blocks reconstructed as fenced Markdown: {summary["codeBlocksRecovered"]}
- TeX blocks recovered from surviving math/tex nodes: {summary["texBlocksRecovered"]}
- Pre-rendered MathJax SVG blocks preserved as raw HTML: {summary["mathJaxSvgBlocksPreserved"]}
- Referenced local assets: {summary["localAssetsReferenced"]}

The generated frontmatter follows current Mizuki fields: title, published,
updated, description, image, tags, category, draft, pinned, comment, author,
sourceLink, and licenseName.

## Move into the new Mizuki site

1. Copy everything under recovered-mizuki/src/content/posts/ into the new
   site's src/content/posts/ directory.
2. Copy the legacy repository's img/ directory into the new site's public/img/
   directory. The recovered Markdown intentionally keeps /img/... URLs.
3. Run the Mizuki build and inspect recovery-report.json and the math-heavy
   posts first.

Example shell commands:

~~~sh
cp -R recovered-mizuki/src/content/posts/* /path/to/new-site/src/content/posts/
cp -R img /path/to/new-site/public/
~~~

## Important note about formulas

A small number of formulas still had original TeX stored in math/tex script
nodes and were restored to dollar-delimited TeX. Many formulas had already
been converted by MathJax into SVG in the deployed HTML; their original TeX no
longer exists in this repository. Those SVG blocks are preserved verbatim as
raw HTML so mathematical content is not silently lost. They can be manually
rewritten to TeX later if desired.

## Audit files

- recovery-report.json: per-post metadata and recovery counts.
- asset-manifest.txt: every referenced local /img/... asset path.
- scripts/recover_hexo_to_mizuki.py: deterministic regeneration script.
"""
    README_PATH.write_text(readme, encoding="utf-8")


def main() -> None:
    if not SOURCE_ROOT.exists():
        raise SystemExit(f"Missing source directory: {SOURCE_ROOT}")

    POSTS_ROOT.mkdir(parents=True, exist_ok=True)

    for old in POSTS_ROOT.glob("*.md"):
        old.unlink()

    html_paths = sorted(SOURCE_ROOT.glob("**/index.html"))
    if len(html_paths) != EXPECTED_POST_COUNT:
        raise SystemExit(
            f"Expected {EXPECTED_POST_COUNT} posts, found {len(html_paths)}"
        )

    all_asset_paths: set[str] = set()
    posts = [extract_post(path, all_asset_paths) for path in html_paths]

    category_counts = Counter(
        post["category"] for post in posts if post["category"]
    )

    summary = {
        "postsRecovered": len(posts),
        "codeBlocksRecovered": sum(p["codeBlocksRecovered"] for p in posts),
        "texBlocksRecovered": sum(p["texBlocksRecovered"] for p in posts),
        "mathJaxSvgBlocksPreserved": sum(
            p["mathJaxSvgBlocksPreserved"] for p in posts
        ),
        "richEmbedsPreserved": sum(
            p["richEmbedsPreserved"] for p in posts
        ),
        "localAssetsReferenced": len(all_asset_paths),
        "categories": dict(sorted(category_counts.items())),
    }

    report = {
        "summary": summary,
        "posts": posts,
    }

    REPORT_PATH.write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    ASSET_MANIFEST_PATH.write_text(
        "\n".join(sorted(all_asset_paths)) + ("\n" if all_asset_paths else ""),
        encoding="utf-8",
    )
    write_readme(report)

    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
