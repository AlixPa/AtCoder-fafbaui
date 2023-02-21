import sys
def IIS(): return map(int, input().split())
def SIS(): return input().split()
def II(): return int(input())
def SI(): return input()
def FIS(): return map(float, input().split())
def FI(): return float(input())
sys.setrecursionlimit(10**8)

n, m = IIS()

vert_ls = [list() for _ in range(n+1)]
vert = [set() for _ in range(n+1)]
for i in range(m):
  u, v = IIS()
  vert[u].add(v)
  vert[v].add(u)
  vert_ls[u].append(v)
  vert_ls[v].append(u)

for i in range(1, n+1):
  m -= (len(vert_ls[i]) - len(vert[i]))

if m != n - 1:
  print("No")
  sys.exit(0)

start = 0
for i in range(1, n+1):
  if len(vert[i]) == 1:
    start = i
    break

seen = [False for _ in range(n+1)]
def dfs(u, i):
  seen[u] = True
  vois = vert[u]
  for v in vois:
    if not seen[v]:
      return dfs(v, i+1)
  return i

depth = dfs(start, 0)
if depth == n-1:
  print("Yes")
else:
  print("No")