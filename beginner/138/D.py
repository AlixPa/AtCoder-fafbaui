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

n, q = IIS()
ls_count = [0 for _ in range(n+1)]
ls_adj = [list() for _ in range(n+1)]
for _ in range(n-1):
  a, b = IIS()
  ls_adj[a].append(b)
  ls_adj[b].append(a)
for _ in range(q):
  p, x = IIS()
  ls_count[p] += x
visited = [False for _ in range(n+1)]
d = deque()
d.append(1)
while d:
  v = d.pop()
  if visited[v]:
    continue
  visited[v] = True
  for neighboor in ls_adj[v]:
    if not visited[neighboor]:
      ls_count[neighboor] += ls_count[v]
      d.append(neighboor)

print(*ls_count[1:])
