# Legacy blog recovery for Astro + Mizuki

This directory is generated from the deployed Hexo HTML in the legacy
repository. The original source/_posts Markdown was not present, so the
recovery is an HTML-to-Markdown reconstruction.

## Recovered content

- Markdown posts: 41
- Code blocks reconstructed as fenced Markdown: 564
- TeX blocks recovered from surviving math/tex nodes: 15
- Pre-rendered MathJax SVG blocks preserved as raw HTML: 2313
- Referenced local assets: 35

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
