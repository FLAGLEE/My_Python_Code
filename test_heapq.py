#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 堆特征
# 位置i处的元素总是大于位置i // 2处的元素（反过来说就是小于位置2 * i和2 * i + 1处的元素）
from heapq import *
from random import shuffle

data = list(range(10))

# 洗牌
shuffle(data)

heap = []

# 函数heappush用于在堆中添加一个元素
for n in data:
    heappush(heap, n)

print(heap)

heappush(heap, 0.5)

print(heap)

# heappop弹出最小的元素（总是位于索引0处），并确保剩余元素中最小的那个位于索引0处（保持堆特征）
print(heappop(heap))
print(heap)

print(heappop(heap))
print(heap)

# 函数heapify通过执行尽可能少的移位操作将列表变成合法的堆（即具备堆特征）
list_heap = [5, 8, 0, 3, 6, 7, 9, 1, 4, 2]
heapify(list_heap)
print(list_heap)
