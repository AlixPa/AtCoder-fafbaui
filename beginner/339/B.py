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

h, w, n = IIS()
grid = [[0 for _ in range(w)] for _ in range(h)]
pos_h = 0
pos_w = 0
direction = 0
for _ in range(n):
  if grid[pos_h][pos_w] == 0:
    grid[pos_h][pos_w] = 1
    direction += 1
  else:
    grid[pos_h][pos_w] = 0
    direction -= 1
  direction %= 4
  if direction == 0:
    pos_h -= 1
  elif direction == 1:
    pos_w += 1
  elif direction == 2:
    pos_h += 1
  else:
    pos_w -= 1
  pos_h %= h
  pos_w %= w

for i in range(h):
  s = ""
  for j in range(w):
    if grid[i][j] == 0:
      s += "."
    else:
      s += "#"
  print(s)
