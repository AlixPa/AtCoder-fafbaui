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

  def addEdge(self, u, v):
    self.graph[u].append(v)
    self.graph[v].append(u)

  def DFSUtil(self, v, visited, color, dt_weight):
    visited.add(v)
    for neighbour in self.graph[v]:
      if neighbour not in visited:
        color[neighbour] = (color[v] + dt_weight[v][neighbour]%2)%2
        self.DFSUtil(neighbour, visited, color, dt_weight)

  def DFS(self, v, dt_weight):
    visited = set()
    color = [0 for _ in range(self.V)]
    self.DFSUtil(v, visited, color, dt_weight)
    return color

n = II()
g = Graph(n)

dt_weight = dict()
for i in range(n):
  dt_weight[i] = dict()
for _ in range(n-1):
  u, v, w = IIS()
  g.addEdge(u-1, v-1)
  dt_weight[u-1][v-1] = w
  dt_weight[v-1][u-1] = w

color = g.DFS(0, dt_weight)
for c in color:
  print(c)