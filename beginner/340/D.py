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
abx = list()
for _ in range(n-1):
  tmp_ls = LIIS()
  abx.append(tmp_ls)

ls_cost = [0]*(n+1)

for i in range(n-1):
  ls_cost[i+2] = ls_cost[i+1] + abx[i][0]

h = [[0, 1]]
nb_e = 1
while nb_e > 0:
  e = heappop(h)
  nb_e -= 1
  if e[0] > ls_cost[e[1]]:
    continue
  ls_cost[e[1]] = e[0]
  if e[1] < n-1:
    heappush(h, [e[0]+abx[e[1]-1][0], e[1]+1])
    nb_e += 1
  if e[1] != n:
    heappush(h, [e[0]+abx[e[1]-1][1], abx[e[1]-1][2]])
    nb_e += 1

print(ls_cost[n])