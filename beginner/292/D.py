import sys
def IIS(): return map(int, input().split())
def SIS(): return input().split()
def II(): return int(input())
def SI(): return input()
def FIS(): return map(float, input().split())
def FI(): return float(input())
sys.setrecursionlimit(10**8)

n, m = IIS()

neighboors = [list() for _ in range(n+1)]
neighboors_st = [set() for _ in range(n+1)]
edges_dt = dict()
for u in range(n+1):
  edges_dt[u] = 0

for _ in range(m):
  u, v = IIS()
  neighboors[u].append(v)
  neighboors[v].append(u)
  neighboors_st[u].add(v)
  neighboors_st[v].add(u)
  edges_dt[u] += 1

seen = [False for _ in range(n+1)]
seen_ls = list()

def dfs(u):
  global seen
  global seen_ls
  seen[u] = True
  seen_ls.append(u)
  neighs = neighboors_st[u]
  for neigh in neighs:
    if not seen[neigh]:
      dfs(neigh)

for u in range(1, n+1):
  seen_ls = list()
  if not seen[u]:
    dfs(u)
  nb_edges = 0
  for v in seen_ls:
    nb_edges += edges_dt[v]
  if nb_edges != len(seen_ls):
    print("No")
    sys.exit(0)

print("Yes")