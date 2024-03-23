from collections import defaultdict

class Graph:
  def __init__(self, vertices):
    self.graph = defaultdict(list)
    self.V = vertices

  def add_edge(self, u, v):
    self.graph[u].append(v)

  def dfs(self, vertex, visited, stack):
    nb = 0
    visited[vertex] = True
    stack.append(vertex)
    for neighbor in self.graph[vertex]:
      if not visited[neighbor]:
        nb += self.dfs(neighbor, visited, stack)
      elif neighbor in stack:
        nb += 1
    stack.pop()
    visited[vertex] = False
    return nb

  def count_simple_cycles(self):
    nb = 0
    visited = [False] * (self.V)
    stack = []
    for vertex in range(self.V):
      nb += self.dfs(vertex, visited, stack)
      visited[vertex] = True
    return nb

if __name__ == "__main__":
  g = Graph(2)
  g.add_edge(0, 1)
  g.add_edge(1, 0)

  g.count_simple_cycles()