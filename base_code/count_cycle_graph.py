from collections import defaultdict

class Graph:
  def __init__(self, vertices):
    self.graph = defaultdict(list)
    self.V = vertices

  def addEdge(self, u, v):
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

  def countCycles(self):
    nb = 0
    visited = [False] * (self.V)
    for v in range(self.V):
      nb += self.dfs(v, v, visited)
      visited[v] = True
    return nb

if __name__ == "__main__":
  g = Graph(2)
  g.addEdge(0, 1)
  g.addEdge(1, 0)

  g.countCycles()