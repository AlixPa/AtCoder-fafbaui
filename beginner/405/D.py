# import copy
# import itertools
# import math
# from bisect import insort, insort_left, insort_right
# from heapq import heapify, heappop, heappush
import sys
from collections import deque

sys.setrecursionlimit(10**8)

h, w = map(int, input().split())
grid = list()
for _ in range(h):
    grid.append([s for s in input()])

filo = deque()
for i in range(h):
    for j in range(w):
        if grid[i][j] == "E":
            filo.append((i, j))

while filo:
    (x, y) = filo.popleft()
    if x > 0:
        if grid[x - 1][y] == ".":
            grid[x - 1][y] = "v"
            filo.append((x - 1, y))
    if x < h - 1:
        if grid[x + 1][y] == ".":
            grid[x + 1][y] = "^"
            filo.append((x + 1, y))
    if y > 0:
        if grid[x][y - 1] == ".":
            grid[x][y - 1] = ">"
            filo.append((x, y - 1))
    if y < w - 1:
        if grid[x][y + 1] == ".":
            grid[x][y + 1] = "<"
            filo.append((x, y + 1))

for s in grid:
    print("".join(s))
