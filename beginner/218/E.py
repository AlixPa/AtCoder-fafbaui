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

class Graph: 
  def __init__(self, vertices): 
    self.V = vertices 
    self.graph = [] 

  def addEdge(self, u, v, w): 
    self.graph.append([u, v, w]) 

  def find(self, parent, i): 
    if parent[i] != i:
      parent[i] = self.find(parent, parent[i]) 
    return parent[i] 

  def union(self, parent, rank, x, y): 
    if rank[x] < rank[y]: 
      parent[x] = y 
    elif rank[x] > rank[y]: 
      parent[y] = x
    else: 
      parent[y] = x 
      rank[x] += 1

  def NonKruskalMST(self):
    result = []
    i = 0
    e = 0 
    self.graph = sorted(self.graph, key=lambda item: item[2])

    parent = []
    rank = []
    for node in range(self.V): 
      parent.append(node) 
      rank.append(0) 
    while e < self.V - 1:
      u, v, w = self.graph[i]
      i += 1
      x = self.find(parent, u) 
      y = self.find(parent, v)
      if x != y: 
        e += 1
        self.union(parent, rank, x, y)
      else:
        result.append(w)

    while i < len(self.graph):
      u, v, w = self.graph[i]
      result.append(w)
      i += 1
    return result

n, m = IIS()
g = Graph(n)
for _ in range(m):
  a, b, c = IIS()
  g.addEdge(a-1, b-1, c)

res = g.NonKruskalMST()
sum_res = 0
for w in res:
  if w > 0:
    sum_res += w
print(sum_res)