---
title: "Mxiaocao 刷题博客总拆解（第一版）"
published: 2026-06-08
updated: 2026-06-08
description: "说明：重点不是复述题解，而是提炼：真正要学什么、下次看到什么条件应该触发什么思路、要不要重做。 重做优先级：高 = 七月冲分重点；中 = 保持手感；低 = 看一眼即可；暂缓 = 当前可先放。 # 题目 来源 真正要学的点 下次触发器 重做 1 A. MEX Table（800） 1. Hello 2025.md MEX 最大化通常先盯住 0；0 同时只能给一行一列提供贡献，答案由较"
image: "/img/2.jpg"
tags: ["总结"]
draft: false
pinned: false
comment: true
author: "Mxiaocao"
sourceLink: "https://www.mxiaocaoblog.com/2026/06/08/Mxiaocao-brush-blog-breakdown-v1/index.html"
licenseName: "CC BY-NC-SA 4.0"
---
说明：重点不是复述题解，而是提炼：真正要学什么、下次看到什么条件应该触发什么思路、要不要重做。

重做优先级：高 = 七月冲分重点；中 = 保持手感；低 = 看一眼即可；暂缓 = 当前可先放。

| # | 题目 | 来源 | 真正要学的点 | 下次触发器 | 重做 |
| --- | --- | --- | --- | --- | --- |
| 1 | A. MEX Table（800） | 1. Hello 2025.md | MEX 最大化通常先盯住 0；0 同时只能给一行一列提供贡献，答案由较长维度决定。 | 看到 MEX + 网格 + 只求最大值，不要构造，先想 0 放哪里、0 能影响几组。 | 低 |
| 2 | B. Gorilla and the Exam（1000） | 1. Hello 2025.md | 把操作目标转化成”保留多少种数”：统计频率，优先用 k 次修改消掉出现次数少的种类。 | 看到可修改元素 + 最小化剩余种类/操作次数，先按频率排序。 | 中 |
| 3 | C. Trip to the Olympiad（1500） | 1. Hello 2025.md | 位运算最大化要按最高不同位拆；高位相同没有贡献，最高不同位以下尽量全贡献。 | 看到三个数/区间/XOR 最大值，先找 l,r 的最高不同位。 | 高 |
| 4 | 1. C - Drop Blocks | Mxiaocao\_Daily\_Compile()(1).md | 全体一起减一可以变成全局偏移量；用”海平面”记录已经整体减过多少。 | 看到每次对所有元素统一减/加，先想懒标记/全局偏移。 | 中 |
| 5 | 2. C - C Stands for Center | Mxiaocao\_Daily\_Compile()(1).md | 枚举中心而不是枚举子串；以 C 为中心的奇长子串个数是左右可扩展最小值。 | 看到奇长子串 + 指定中点，先枚举中点。 | 低 |
| 6 | 3. D - Adjacent Distinct String | Mxiaocao\_Daily\_Compile()(1).md | 重排避免相邻相同，不能简单轮流放；高频字符要先放奇偶位隔开。 | 看到重排 + 相邻不能相同，先看最大频率，考虑隔位填。 | 中 |
| 7 | 4. D - Chalkboard Median | Mxiaocao\_Daily\_Compile()(1).md | 动态中位数用两个堆维护左右半区，保持大小平衡。 | 看到在线插入 + 查询中位数，直接双堆。 | 中 |
| 8 | 5. C - Sushi | Mxiaocao\_Daily\_Compile()(1).md | 排序后双指针/贪心匹配，小的需求优先匹配能满足它的最小资源。 | 看到两个数组配对最大数量，先排序双指针。 | 低 |
| 9 | 6. C - Long Sequence | Mxiaocao\_Daily\_Compile()(1).md | 重复拼接的大序列不要真的展开，按块长度和前缀累计定位。 | 看到数组重复很多次 + 查询第 k 个，先做块长度/前缀和定位。 | 中 |
| 10 | 7. D - Raise Minimum | Mxiaocao\_Daily\_Compile()(1).md | 最大化最小值通常二分答案，也可以用堆模拟；本质是检查能否把所有数抬到 mid。 | 看到最大化最小值 + 次数限制，先二分答案。 | 中 |
| 11 | 8. C - Not Adjacent | Mxiaocao\_Daily\_Compile()(1).md | 相邻限制题先转化成奇偶/间隔位置，判断能否隔开放。 | 看到不能相邻，先想位置间隔、奇偶格。 | 中 |
| 12 | 9. D - Not Adjacent 2 | Mxiaocao\_Daily\_Compile()(1).md | 相邻限制加强版通常从简单版推广：先找局部约束，再考虑计数/构造。 | 看到同题 Hard，要先问 easy 的核心不变量是否还能维护。 | 高 |
| 13 | 10. C - Vanish | Mxiaocao\_Daily\_Compile()(1).md | 过程题先找每个元素什么时候消失/贡献，不要逐步模拟。 | 看到反复删除/消失，先找单个对象的生命周期。 | 中 |
| 14 | A. Koshary | 26\_4\_30 Codeforces Round 1096 (Div. 3).md | 坐标可达性就是奇偶性问题；长步改变 2，短步最多改变一次奇偶。 | 看到只能 +2 且最多一次 +1，先看奇偶个数。 | 低 |
| 15 | 1. C1. Equal Multisets (Easy Version) | Mxiaocao\_Daily\_Compile().md | 滑动窗口多重集相同会强制窗口滑出/滑入元素一致；中间才是自由区。 | 看到所有长度 k 窗口多重集匹配，比较相邻窗口的差异。 | 高 |
| 16 | 2. B. Array and Permutation（1100） | Mxiaocao\_Daily\_Compile().md | 复制操作会让每个值扩散成连续块；目标数组每个值的来源位置必须落在对应连续段里。 | 看到相邻复制/扩散，想连续块和来源点。 | 高 |
| 17 | 3. C. Dice Roll Sequence（1100） | Mxiaocao\_Daily\_Compile().md | 骰子/序列计数先定义状态，或者从小样例猜递推；不要硬模拟所有序列。 | 看到固定规则数序列，先写 dp 状态或打表找递推。 | 中 |
| 18 | 4. B. Cyclists（1100） | Mxiaocao\_Daily\_Compile().md | 圆/环上相对位置问题先转化成距离和方向，避免坐标模拟。 | 看到环形追赶/位置，先算最短距离或相对速度。 | 中 |
| 19 | A. Two Frogs（800） | 3. Codeforces Round 996 (Div. 2).md | 博弈小题常是奇偶性；先画小 n，看先手是否由距离奇偶决定。 | 看到两人轮流移动且必须移动，打表小状态找奇偶。 | 中 |
| 20 | B. Crafting（1000） | 3. Codeforces Round 996 (Div. 2).md | 资源转换题先看缺口数量；多个负缺口通常不可能，一个负缺口再看其他资源是否够扣。 | 看到一个资源增加、其他全部减少，先看 a-b 的负数个数。 | 高 |
| 21 | C. The Trail（1400） | 3. Codeforces Round 996 (Div. 2).md | 路径上未知值可用行列和约束反推；当下一步离开某行/列时把它补成目标和。 | 看到矩阵行列和 + 路径未知，先想按路径顺序消行/消列。 | 高 |
| 22 | 11. D - Card Pile Query | MxiaocaoDaily\_Compile() T11.md | 只记录每张牌下面是谁，最后用类似并查集找底牌统计堆大小。 | 看到堆叠/链式关系，存 parent/down 指针，最后路径压缩。 | 中 |
| 23 | 12. C - Variety | MxiaocaoDaily\_Compile() T11.md | 博客内容不完整，暂时只标记：需要补题意、关键结论、触发器。 | 笔记空白就是复盘断点，先补完整。 | 高 |
| 24 | A. Convergence | 26\_5\_30 Codeforces Round 1101 (Div. 2).md | 选目标点时，代价由左右两边人数最大值决定；枚举不同坐标并维护左右计数。 | 看到所有点汇合到某个已有坐标，先排序/计数左右人数。 | 中 |
| 25 | B. Cake Leveling | 26\_5\_30 Codeforces Round 1101 (Div. 2).md | 前缀能均分的最大高度由前缀平均值下界决定；答案是历史最小 floor(prefix\_sum/i)。 | 看到每个前缀的最大统一高度，先看前缀和/平均值。 | 中 |
| 26 | C1. Seating Arrangement (Easy Version) | 26\_5\_30 Codeforces Round 1101 (Div. 2).md | 座位资源分两类：空桌和残缺位；A 类选择可反悔，贪心要维护资源。 | 看到 I/E/A 这种可选身份，先把每类人对资源的消耗/产出写清楚。 | 高 |
| 27 | A. Optimal Purchase | 26\_5\_18 Educational Codeforces Round 190 (Rated for Div. 2).md | 分组购买题先比较整组和散买，余数再单独比较。 | 看到每 3 个一组优惠，先 n/3、n%3 分类。 | 低 |
| 28 | B. Digit String | 26\_5\_18 Educational Codeforces Round 190 (Rated for Div. 2).md | 整除 4 的子序列只看最后一位或最后两位；先写判定性质再考虑删除。 | 看到数字串 + 倍数/整除，先想末位规则。 | 高 |
| 29 | C. Arrange the Numbers in a Circle | 26\_5\_18 Educational Codeforces Round 190 (Rated for Div. 2).md | 圆排列避免坏模式，先按出现次数分块，频率>=2 的数适合作为缓冲块。 | 看到圆排列 + 连续若干个限制，先按频率分块。 | 高 |
| 30 | A. Anxiety at the restaurant | Team Weekly Contest 2026-5-10.md | 向上取整不要用浮点数，用 (a+b-1)/b。 | 看到百分比/ceil，先整数化。 | 低 |
| 31 | G. Gerald the mudcrab | Team Weekly Contest 2026-5-10.md | 最少替换成排列就是缺多少种数；答案 n - distinct。 | 看到要变成 1..n 每种一个，先数不同元素。 | 低 |
| 32 | J. Just the right enchantment | Team Weekly Contest 2026-5-10.md | 组合计数先按奇偶分类；和为偶只可能三偶或一偶二奇。 | 看到三元组和的奇偶，先按奇偶计数再组合数。 | 中 |
| 33 | E. Erasmus Valthron | Team Weekly Contest 2026-5-10.md | 把数字按质因子生成关系看成树/DAG，从 1 出发乘质数扩展。 | 看到数字可由乘质因子生成，先想因子树/DFS。 | 高 |
| 34 | I. Inner Product | Team Weekly Contest 2026-5-10.md | 不等式关系串先转成相对高度，再整体平移到正数；另一个序列可独立优化。 | 看到 < > = 约束构造，先建差分高度。 | 高 |
| 35 | B. Bad LaTeX | Team Weekly Contest 2026-5-10.md | 字符串处理题先保护不能改的区间，再对未保护字符做规则。 | 看到括号/转义/保护区，先标记受保护位置。 | 中 |
| 36 | A. Shape Perimeter（800） | 2. Codeforces Round 996 (Div. 2).md | 连续印章且保证连通，新增周长 = 新方块周长 - 重叠边贡献。 | 看到图形并集周长，先算每次新增和重叠。 | 中 |
| 37 | B. Find the Permutation（1300） | 2. Codeforces Round 996 (Div. 2).md | 邻接矩阵表示两元素先后关系，可以把比较函数转成排序/计数排名。 | 看到图由隐藏排列生成，先解释 g[i][j] 对 i,j 相对顺序的含义。 | 高 |
| 38 | C. Palindromic Subsequences（1200） | 2. Codeforces Round 996 (Div. 2).md | 构造题别只猜样例，要明确回文子序列条件被哪些值触发。 | 看到要求构造避免/满足回文子序列，先找最短坏模式。 | 中 |
| 39 | A. Marisa Steals Reimu’s Takeout | 26\_5\_17 Codeforces Round 1098 (Div. 2).md | 模 3 删除最大次数：0 单独贡献，1+2 配对，剩余同类三个一组。 | 看到值域 0/1/2 + 和被 3 整除，先计数取模。 | 低 |
| 40 | B. Remilia Plays Soku | 26\_5\_17 Codeforces Round 1098 (Div. 2).md | 环上追逐不能只加 k，要考虑两条方向和目标选择；先严格画时间顺序。 | 看到博弈追逐 + 圆，先算两边距离并检查回合顺序。 | 高 |
| 41 | C1. Cirno and Number (Easy Version) | 26\_5\_17 Codeforces Round 1098 (Div. 2).md | easy 可 DFS 枚举，但要注意状态边界；hard 可能要数位 DP。 | 看到对数字做位操作且 n 小，先 DFS；n 大再数位 DP。 | 中 |
| 42 | 1. A. Was there an Array? | 5. Educational Codeforces Round 174 (Rated for Div. 2).md | 局部约束题要找完整最小矛盾模式：这里只是 101，不是 1?1。 | 看到 b[i] 表示邻域性质，枚举长度 3 的 b 模式。 | 高 |
| 43 | 2. B. Set of Strangers | 5. Educational Codeforces Round 174 (Rated for Div. 2).md | 按颜色独立算消除代价：无相邻为 1，有相邻为 2，最后保留最大代价颜色。 | 看到同色 + 不相邻操作，单独分析每种颜色的代价。 | 高 |
| 44 | 3. C. Beautiful Sequence | 5. Educational Codeforces Round 174 (Rated for Div. 2).md | 值域只有 1/2/3，先推合法子序列只能是 1 + 若干 2 + 3，再状态机计数。 | 看到小值域 + 合法子序列计数，先分析形态。 | 高 |
| 45 | A. Kevin and Arithmetic | 4. IAEPC Preliminary Contest (Codeforces Round 999, Div. 1 + Div. 2).md | 重排最大化分数，先分析奇偶状态变化；偶数开头可最大化后续奇数贡献。 | 看到加和后按奇偶得分，先看当前 sum 奇偶如何转移。 | 中 |
| 46 | B. Kevin and Geometry | 4. IAEPC Preliminary Contest (Codeforces Round 999, Div. 1 + Div. 2).md | 等腰梯形通常需要一对相等腰，再找两条底满足差值小于 2\*腰。 | 看到从木棍选四个成图形，先找成对长度，再用排序检查不等式。 | 高 |
| 47 | 11. Beautiful String（1000） | codefoces mind (T11-20).md | 输出任意方案时可以极端构造：删所有 0，剩下全 1 必回文，删的子序列也非降。 | 看到任意子序列 + 剩余串性质，先试删一整类字符。 | 高 |
| 48 | 12. Loyalty（1200） | codefoces mind (T11-20).md | 跨越 floor(S/X) 边界时赚当前物品，贪心用小物品铺垫，大物品跨线。 | 看到前缀和跨阈值奖励，先排序双指针：小的填坑，大的领奖。 | 高 |
| 49 | 13. Split（1200） | codefoces mind (T11-20).md | 拆分奇偶类题要先推每种数能产生的贡献，而不是直接按样例猜。 | 看到数的拆分 + 奇偶，先列奇数/偶数可拆成什么。 | 中 |
| 50 | 14. Palindromex（） | codefoces mind (T11-20).md | 你当时其实有分类入口；这类题要敢把 X/Y/都没有三类写完。 | 看到字符串只关心特殊字符，先按特殊字符出现情况分类。 | 中 |
| 51 | 15. Abraham’s Great Escape（1100） | codefoces mind (T11-20).md | 小网格构造先打表找唯一不可能形态，再给通用构造。 | 看到网格构造 + 小 k，先打表 3x3/4x4 找例外。 | 中 |
| 52 | 16. The Sports Festival（1800） | codefoces mind (T11-20).md | 区间 DP：排序后从两端扩展已选集合，代价由当前区间 max-min 决定。 | 看到每次选一个导致当前 max-min 代价，先排序 + 区间 DP。 | 高/暂缓 |
| 53 | 17. Zhily and Mex and Max（） | codefoces mind (T11-20).md | 同时最大化 max 和 mex 时，把最大值前置，再按 0,1,2… 保证 mex。 | 看到 mex 和 max 同时出现，先分开满足两个目标。 | 中 |
| 54 | 18. Zhily and Bracket Swapping（） | codefoces mind (T11-20).md | 括号串问题先转前缀和；交换影响的是前缀平衡和总和。 | 看到括号 + swap，先把 ‘(‘=1, ‘)’=−1，看总和和最小前缀。 | 高 |
| 55 | 19. Multiple Construction（1000） | codefoces mind (T11-20).md | 距离/重复位置构造要从小 n 打表，观察数字 i 出现位置间距。 | 看到构造排列且有距离要求，先打表小 n 找放置顺序。 | 中 |
| 56 | 20. Maximum Cost Permutation（1000） | codefoces mind (T11-20).md | 含 0 排列题先找需要修复的最小区间：从最左错位到最右错位。 | 看到 permutation + 0/错位，先定位错误区间。 | 中 |
| 57 | D. Dungeon Equilibrium | Team Weekly Contest 2026-5-16.md | 平衡条件是值 x 必须保留恰好 x 个；按频率独立决策删到 0 或删到 x。 | 看到每个值的数量必须等于值本身，统计频率逐值算代价。 | 中 |
| 58 | E. Expansion Plan 2 | Team Weekly Contest 2026-5-16.md | 网格扩张查询要把操作转成距离度量：4 是曼哈顿扩张，8 是切比雪夫/对角扩张。 | 看到网格扩张 + 多查询，先找一次操作对应的距离球。 | 高 |
| 59 | F. Factory Table | Team Weekly Contest 2026-5-16.md | 内容不足，先补题意和正解；暂时不纳入重做优先级。 | 笔记空白说明当时没有沉淀，先补关键结论。 | 中 |
| 60 | 21. XOR Array（1300） | codeforces mind（T21-30).md | 区间 XOR 为 0 等价于前缀异或相等；只让指定两个前缀相等，其余前缀互异。 | 看到只有一个子区间 XOR 为 0，立刻转前缀异或。 | 高 |
| 61 | 22. Cyclic Merging（1300） | codeforces mind（T21-30).md | 环形合并题先断环/旋转，再考虑双端队列维护可合并顺序。 | 看到 cyclic + merging，先想旋转等价和断环。 | 高 |
| 62 | 1. The 67th XOR Problem（1200） | codefoces mind (T1-10).md | 操作过程先展开几步找抵消，最后只剩”最后被选”和”未被选”两数异或。 | 看到 XOR + 多步操作，先手推 2~3 步，不要先排序贪心。 | 高 |
| 63 | 2. The 67th OEIS Problem（1100） | codefoces mind (T1-10).md | 构造 gcd 不同，可先构造辅助 b，让 a[i]=b[i]b[i+1]，把 gcd 控制成 b[i+1]。 | 看到相邻 gcd 构造，考虑乘积辅助序列。 | 高 |
| 64 | 3. Mickey Mouse Constructive（1100） | codefoces mind (T1-10).md | 构造 + 计数函数题，要先找 f(a) 由什么决定；这里由 /x-y/ 的因子数决定。 | 看到 +1/-1 排列和分段和，先看总和与因子。 | 高 |
| 65 | 4. Flipping Binary String（1000） | codefoces mind (T1-10).md | 翻转次数只看奇偶；能否全 0 要转成每位翻转奇偶约束。 | 看到反复翻转同一位，先把次数 mod 2。 | 中 |
| 66 | 5. MEX Reordering（1000） | codefoces mind (T1-10).md | MEX 题先盯住 0 和 1 的相对位置，判断不可构造的最小坏条件。 | 看到重排影响 MEX，先检查 0、1、缺失数。 | 中 |
| 67 | 6. Sorting Game（1200） | codefoces mind (T1-10).md | 游戏题先看是否已经有序；若先手能一次选所有错位位置，则直接赢。 | 看到二进制串排序游戏，比较原串和排序串的错位集合。 | 中 |
| 68 | 7. The Curse of the Frog（1200） | codefoces mind (T1-10).md | 周期前进题先算不回撤能否到达，再看每轮最大净前进。 | 看到跳跃+回撤+重复，先算单轮净收益。 | 中 |
| 69 | 8.Yet Another MEX Problem（1100） | codefoces mind (T1-10).md | 删除/操作最大化 MEX 时，先定位 0 和当前 mex，再分析操作影响。 | 看到 MEX + 删除，先找当前 mex 和缺失位置。 | 高 |
| 70 | 9.Blackslex and Penguin Civilization（1300）（×） | codefoces mind (T1-10).md | 按位与前缀会不断丢 1；popcount 限制等价于锁定若干二进制位。 | 看到前缀 AND + popcount，想”锁死位数”和自由位。 | 高/暂缓 |
| 71 | 10. Beautiful XOR（1100） | codefoces mind (T1-10).md | 位运算变换题先比较 a,b 的最高不同位，判断能否通过操作消掉。 | 看到 a->b 的 XOR/bit 操作，先看最高不同位和大小关系。 | 中 |
| 72 | 1\_E. Product Queries（1300） | codeforces problemset集训(1200-1400).md | 把能选的数看成乘法边，求乘积到每个 i 的最短步数，本质是因子图 BFS。 | 看到重复选择数组元素凑乘积，先想 BFS/最短路，状态是当前乘积。 | 高 |
| 73 | 2\_B. ABAB Construction (1200) | codeforces problemset集训(1200-1400).md | 交替串博弈/构造要看长度奇偶；偶长端点不同，连续两步凑一对。 | 看到 AB 交替 + 取两端，先分析奇偶长度的端点字符。 | 中 |
| 74 | 3\_A1. Lost Civilization (Easy Version) (1300) | codeforces problemset集训(1200-1400).md | 栈维护结构：当新元素破坏末尾模式时弹出，类似单调栈/规约。 | 看到序列逐步合并/删除模式，先想栈。 | 中 |
