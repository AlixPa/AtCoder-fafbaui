import sys, math, copy, itertools
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

n = II()
ls_xy = list()
for _ in range(n):
  x, y = IIS()
  ls_xy.append((x, y))
for i in range(n):
  max_dist = -math.inf
  max_index = -1
  xi, yi = ls_xy[i]
  for j in range(n):
    if i == j:
      continue
    xj, yj = ls_xy[j]
    if pow(xi-xj, 2) + pow(yi - yj, 2) > max_dist:
      max_dist = pow(xi-xj, 2) + pow(yi - yj, 2)
      max_index = j
  print(max_index+1)