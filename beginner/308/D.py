# import copy
# import itertools
# import math
# from bisect import insort, insort_left, insort_right
# from heapq import heapify, heappop, heappush
import sys
from collections import defaultdict, deque

sys.setrecursionlimit(10**8)

h, w = map(int, input().split())
grid = list()
for _ in range(h):
    grid.append(input())

fifo: deque = deque()
seen = [[False] * w for _ in range(h)]
keyword = "snuke"
next = {keyword[i]: keyword[(i + 1) % 5] for i in range(5)}
fifo.append((0, 0))
while fifo:
    x, y = fifo.popleft()
    if seen[x][y]:
        continue
    seen[x][y] = True
    if grid[x][y] in next:
        to_be = next[grid[x][y]]
    else:
        continue
    if x > 0:
        if not seen[x - 1][y] and grid[x - 1][y] == to_be:
            fifo.append((x - 1, y))
    if x < h - 1:
        if not seen[x + 1][y] and grid[x + 1][y] == to_be:
            fifo.append((x + 1, y))
    if y > 0:
        if not seen[x][y - 1] and grid[x][y - 1] == to_be:
            fifo.append((x, y - 1))
    if y < w - 1:
        if not seen[x][y + 1] and grid[x][y + 1] == to_be:
            fifo.append((x, y + 1))
print("Yes" if seen[-1][-1] else "No")
