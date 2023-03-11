import sys, math
from collections import deque
def IIS(): return map(int, input().split())
def SIS(): return input().split()
def II(): return int(input())
def SI(): return input()
def FIS(): return map(float, input().split())
def FI(): return float(input())
sys.setrecursionlimit(10**8)

h, w = IIS()
grid = list()
for _ in range(h):
  ls_w = list(IIS())
  grid.append(ls_w)

def newPath(pos_h, pos_w, set_seen):
  if pos_h >= h:
    return 0
  if pos_w >= w:
    return 0
  if grid[pos_h][pos_w] in set_seen:
    return 0
  if pos_h == (h-1) and pos_w == (w-1):
    return 1
  set_copy1 = set_seen.copy()
  set_copy1.add(grid[pos_h][pos_w])
  set_copy2 = set_seen.copy()
  set_copy2.add(grid[pos_h][pos_w])
  return newPath(pos_h=pos_h+1, pos_w=pos_w, set_seen=set_copy1) + newPath(pos_h=pos_h, pos_w=pos_w+1, set_seen=set_copy2)

print(newPath(pos_h=0, pos_w=0, set_seen=set()))