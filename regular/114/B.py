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

class Graph:
  def __init__(self, vertices):
    self.graph = defaultdict(list)
    self.V = vertices

  def add_edge(self, u, v):
    self.graph[u].append(v)

  def dfs(self, v1, v, visited):
    nb = 0
    if visited[v]:
      if(v1 == v):
        return 1
      return 0
    visited[v] = True

    for x in self.graph[v]:
      nb += self.dfs(v1, x, visited)
    visited[v] = False
    return nb

  def allCycles(self):
    nb = 0
    visited = [False] * (self.V)
    for v in range(self.V):
      nb += self.dfs(v, v, visited)
      visited[v] = True
    return nb

MOD = 998244353
n = II()
ls_f = LIIS()
g = Graph(n)
for i in range(n):
  g.add_edge(i, ls_f[i]-1)

nb_cycle = g.allCycles()
res = (pow(2, nb_cycle, MOD) - 1)%MOD
print(res)