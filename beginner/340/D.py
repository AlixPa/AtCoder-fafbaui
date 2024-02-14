import sys, math
from collections import deque
from heapq import heappop, heappush
from numpy import Inf
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
abx = list()
graph = dict()
for i in range(n):
  graph[i] = list()
for i in range(n-1):
  a, b, x = IIS()
  graph[i].append((i+1, a))
  graph[i].append((x-1, b))

def lazyDijkstras(graph, root):
  n = len(graph)
  dist = [Inf for _ in range(n)]
  dist[root] = 0
  visited = [False for _ in range(n)]
  pq = [(0, root)]
  while len(pq) > 0:
    _, u = heappop(pq)
    if visited[u]:
      continue
    visited[u] = True
    for v, l in graph[u]:
      if dist[u] + l < dist[v]:
        dist[v] = dist[u] + l
        heappush(pq, (dist[v], v))
  return dist

print(lazyDijkstras(graph,0)[n-1])