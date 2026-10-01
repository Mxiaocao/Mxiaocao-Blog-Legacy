---
title: "2.1.8 deque"
published: 2026-05-14
updated: 2026-05-30
description: "2.1.8 dequedeque(双端队列)支持两端 O(1)插入/删除，比vector更适合做队头操作，比queue/stack更灵活。 deque常见用途 普通队列（push_back + pop_front) 双端操作（回文、窗口） 单调队列（滑动窗口最值） 0-1 BFS 一、结构二、初始化头文件：<bits/stdc++.h> or <deque> 12345"
image: "/img/2.jpg"
tags: ["deque", "stl"]
category: "stl"
draft: false
pinned: false
comment: true
author: "Mxiaocao"
sourceLink: "https://www.mxiaocaoblog.com/2026/05/14/2-1-8-deque/index.html"
licenseName: "CC BY-NC-SA 4.0"
---
# 2.1.8 deque

deque(双端队列)支持两端 O(1)插入/删除，比vector更适合做队头操作，比queue/stack更灵活。

deque常见用途

- 普通队列（push\_back + pop\_front)
- 双端操作（回文、窗口）
- 单调队列（滑动窗口最值）
- 0-1 BFS

## 一、结构

## 二、初始化

头文件：`<bits/stdc++.h> or <deque>`


```cpp
deque<int> d1;  //空
deque<int> d2(5);  //5个0
deque<int> d3(5,7);  //5个7
deque<int> d4 = {1,2,3,4};  //列表初始化
deque<int> d5(d4.begin(),d4.end());  //迭代器
```


## 三、基本操作

### 1. 两端插入/删除


```cpp
d.push_back(x);
d.push_front(x);
d.pop_back();
d.pop_front();
```


### 2. 访问元素


```cpp
d.front();
d.back();
d[i];
d.at(i);
```


### 3.容量相关

**相关文章**

[[2-1-5-priority-queue]]
