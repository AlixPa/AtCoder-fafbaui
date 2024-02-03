import sys, math
from collections import deque
from heapq import heappop, heappush
def IIS(): return map(int, input().split())
def LIIS(): return list(IIS())
def SIIS(): return set(IIS())
def SIS(): return input().split()
def II(): return int(input())
def SI(): return input()
def FIS(): return map(float, input().split())
def FI(): return float(input())
sys.setrecursionlimit(10**8)

n = II()
x1 = -1
y1 = -1
x2 = -1
y2 = -1
grid = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
  s = SI()
  for j in range(n):
    if s[j] == "#":
      grid[i][j] = 1
    if s[j] == "P":
      if x1 == -1:
        x1 = i
        y1 = j
      else:
        x2 = i
        y2 = j

ls_same_pos = [[[[0  for _ in range(n)] for _ in range(n)] for _ in range(n)] for _ in range(n)]
d_pos = deque()
d_pos.append((0, x1, y1, x2, y2))
nb_elem = 1
while(True):
  if nb_elem == 0:
    print(-1)
    sys.exit(0)
  step, x1, y1, x2, y2 = d_pos.pop()
  nb_elem -= 1
  if x1 == x2 and y1 == y2:
    print(step)
    sys.exit(0)
  if ls_same_pos[x1][y1][x2][y2] == 1:
    continue
  ls_same_pos[x1][y1][x2][y2] = 1
  if x1 < n-1 or x2 < n-1:
    new_x1 = min(x1 + 1, n-1)
    new_x2 = min(x2 + 1, n-1)
    if grid[new_x1][y1] == 1:
      new_x1 = x1
    if grid[new_x2][y2] == 1:
      new_x2 = x2
    if new_x1 != x1 or new_x2 != x2:
      d_pos.appendleft((step + 1, new_x1, y1, new_x2, y2))
      nb_elem += 1
  if x1 > 0 or x2 > 0:
    new_x1 = max(x1 - 1, 0)
    new_x2 = max(x2 - 1, 0)
    if grid[new_x1][y1] == 1:
      new_x1 = x1
    if grid[new_x2][y2] == 1:
      new_x2 = x2
    if new_x1 != x1 or new_x2 != x2:
      d_pos.appendleft((step + 1, new_x1, y1, new_x2, y2))
      nb_elem += 1
  if y1 < n-1 or y2 < n-1:
    new_y1 = min(y1 + 1, n-1)
    new_y2 = min(y2 + 1, n-1)
    if grid[x1][new_y1] == 1:
      new_y1 = y1
    if grid[x2][new_y2] == 1:
      new_y2 = y2
    if new_y1 != y1 or new_y2 != y2:
      d_pos.appendleft((step + 1, x1, new_y1, x2, new_y2))
      nb_elem += 1
  if y1 > 0 or y2 > 0:
    new_y1 = max(y1 - 1, 0)
    new_y2 = max(y2 - 1, 0)
    if grid[x1][new_y1] == 1:
      new_y1 = y1
    if grid[x2][new_y2] == 1:
      new_y2 = y2
    if new_y1 != y1 or new_y2 != y2:
      d_pos.appendleft((step + 1, x1, new_y1, x2, new_y2))
      nb_elem += 1
  