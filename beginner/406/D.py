# import copy
# import itertools
# import math
# from bisect import insort, insort_left, insort_right
# from collections import defaultdict, deque
# from heapq import heapify, heappop, heappush
import sys

sys.setrecursionlimit(10**8)
h, w, n = map(int, input().split())

dt_row = {i: set() for i in range(h + 1)}
dt_col = {i: set() for i in range(w + 1)}

for _ in range(n):
    x, y = map(int, input().split())
    dt_row[x].add(y)
    dt_col[y].add(x)

seen = set()
q = int(input())
for _ in range(q):
    t, pos = map(int, input().split())
    if t == 1:
        st_col = dt_row[pos]
        dt_row[pos] = set()
        cnt = 0
        for col in st_col:
            if (pos, col) in seen:
                continue
            cnt += 1
            seen.add((pos, col))
        print(cnt)
    if t == 2:
        st_row = dt_col[pos]
        dt_col[pos] = set()
        cnt = 0
        for row in st_row:
            if (row, pos) in seen:
                continue
            cnt += 1
            seen.add((row, pos))
        print(cnt)
