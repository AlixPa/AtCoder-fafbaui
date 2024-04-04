import sys, math
from collections import deque, defaultdict
from heapq import heappop, heappush, heapify
def IIS(): return map(int, input().split())
def LIIS(): return list(IIS())
def SIIS(): return set(IIS())
def SIS(): return input().split()
def II(): return int(input())
def SI(): return input()
def FIS(): return map(float, input().split())
def FI(): return float(input())
sys.setrecursionlimit(10**8)

def move(grid, grid_steps, pos, h, w):
  i, j = pos
  if i < h-1 and grid[i+1][j] == "." and grid_steps[i][j] + 1 < grid_steps[i+1][j]:
    grid_steps[i+1][j] = grid_steps[i][j] + 1
    move(grid, grid_steps, (i+1, j), h, w)
  if i > 0 and grid[i-1][j] == "." and grid_steps[i][j] + 1 < grid_steps[i-1][j]:
    grid_steps[i-1][j] = grid_steps[i][j] + 1
    move(grid, grid_steps, (i-1, j), h, w)
  if j < w-1 and grid[i][j+1] == "." and grid_steps[i][j] + 1 < grid_steps[i][j+1]:
    grid_steps[i][j+1] = grid_steps[i][j] + 1
    move(grid, grid_steps, (i, j+1), h, w)
  if j > 0 and grid[i][j-1] == "." and grid_steps[i][j] + 1 < grid_steps[i][j-1]:
    grid_steps[i][j-1] = grid_steps[i][j] + 1
    move(grid, grid_steps, (i, j-1), h, w)

h, w = IIS()
grid = list()
for _ in range(h):
  s = SI()
  grid.append(s)
grid_steps = [[math.inf for _ in range(w)] for _ in range(h)]
grid_steps[0][0] = 1

move(grid, grid_steps, (0,0), h, w)

nb_w = 0
for i in range(h):
  for j in range(w):
    if grid[i][j] == ".":
      nb_w += 1

if grid_steps[-1][-1] != math.inf:
  print(nb_w - grid_steps[-1][-1])
else:
  print(-1)