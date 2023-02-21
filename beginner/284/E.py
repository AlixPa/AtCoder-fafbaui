def IIS(): return map(int, input().split())
def SIS(): return input().split()
def II(): return int(input())
def SI(): return input()
def FIS(): return map(float, input().split())
def FI(): return float(input())

n,m = IIS()

links = [set() for i in range(n+1)]
seen = [False]*(n+1)
nb = 0

for i in range(m):
  u,v = IIS()
  links[u].add(v)
  links[v].add(u)

import sys
sys.setrecursionlimit(10**8)
def dfs(u):
  global nb, seen, links
  nb += 1
  if nb == 10**6:
    print(nb)
    sys.exit(0)
  seen[u] = True
  for v in links[u]:
    if not seen[v]:
      dfs(v)
  seen[u] = False
  return nb

print(dfs(1))