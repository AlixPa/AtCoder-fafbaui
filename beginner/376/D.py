import sys, math, copy, itertools
from bisect import insort, insort_left, insort_right
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

n, m = IIS()
ls_edges = [list() for _ in range(n)]
ls_dist = [0 for _ in range(n)]
dq = deque([0])

for _ in range(m):
  u, v = IIS()
  ls_edges[u-1].append(v-1)

while len(dq) > 0 and ls_dist[0] == 0:
  u = dq.pop()
  for v in ls_edges[u]:
    if ls_dist[v] == 0:
      ls_dist[v] = ls_dist[u] + 1
      dq.appendleft(v)
    if v == 0:
      break
      

if ls_dist[0] != 0:
  print(ls_dist[0])
else:
  print(-1)
