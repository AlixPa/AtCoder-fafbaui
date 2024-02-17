import sys, math
from collections import deque, defaultdict
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
t = SI()
ls_terrain = list()
for _ in range(h):
  s = SI()
  ls_terrain.append(s)
pos_land = list()
for i in range(h):
  for j in range(w):
    if ls_terrain[i][j] == ".":
      pos_land.append((i, j))
nb_good = 0
for (x, y) in pos_land:
  good = True
  for move in t:
    if move == "L":
      y -= 1
    elif move == "R":
      y += 1
    elif move == "U":
      x -= 1
    else:
      x += 1
    if x < 1 or x >= h-1 or y < 1 or y >= w-1 or ls_terrain[x][y] == "#":
      good = False
      break
  if good:
    nb_good += 1

print(nb_good)