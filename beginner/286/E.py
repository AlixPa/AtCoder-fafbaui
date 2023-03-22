import sys, math
from collections import deque
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

n = II()
ls_a = [0] + LIIS()
ls_s = [""] + [SI() for _ in range(n)]

TPST = pow(10,16)
dist_value = [[[TPST, 0] for _ in range(n+1)] for _ in range(n+1)]
for i in range(1, n+1):
  for j in range(1, n+1):
    if ls_s[i][j-1] == "Y":
      dist_value[i][j][0] = 1
      dist_value[i][j][1] = ls_a[i] + ls_a[j]
    elif i == j:
      dist_value[i][j][0] = 0
      dist_value[i][j][1] = ls_a[i]

for k in range(1, n+1):
  for i in range(1, n+1):
    for j in range(1, n+1):
      if dist_value[i][j][0] > dist_value[i][k][0] + dist_value[k][j][0]:
        dist_value[i][j][0] = dist_value[i][k][0] + dist_value[k][j][0]
        dist_value[i][j][1] = dist_value[i][k][1] + dist_value[k][j][1] - ls_a[k]
      elif dist_value[i][j][0] == dist_value[i][k][0] + dist_value[k][j][0] and dist_value[i][j][1] < dist_value[i][k][1] + dist_value[k][j][1] - ls_a[k]:
        dist_value[i][j][1] = dist_value[i][k][1] + dist_value[k][j][1] - ls_a[k]

q = II()
for _ in range(q):
  u, v = IIS()
  if dist_value[u][v][0] == TPST:
    print("Impossible")
  else:
    print(*dist_value[u][v])