from collections import defaultdict

# DIRECTED
class Graph:
  def __init__(self, vertices):
    self.graph = defaultdict(list)
    self.V = vertices

  # CHANGE HERE TO UNDIRECTED
  def addEdge(self, u, v):
    self.graph[u].append(v)

  def DFSUtil(self, v, visited):
    visited.add(v)
    # DO WHATEVER YOU WANT HERE
    print(v, end=' ')
    for neighbour in self.graph[v]:
      if neighbour not in visited:
        self.DFSUtil(neighbour, visited)

  def DFS(self, v):
    visited = set()
    self.DFSUtil(v, visited)

if __name__ == "__main__":
  g = Graph(3)
  g.addEdge(0, 1)
  g.addEdge(0, 2)
  g.addEdge(1, 2)
  g.addEdge(2, 0)
  g.addEdge(2, 3)
  g.addEdge(3, 3)

  g.DFS(2)
