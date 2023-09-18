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

def expload(bij, i, j, r, c):
  power = int(bij[i][j])
  for n in range(max(i-power, 0), min(i+power+1, r)):
    for m in range(max(j-power, 0), min(j+power+1, c)):
      if abs(n-i)+abs(m-j) > power:
        continue
      if bij[n][m] == "#":
        bij[n] = bij[n][:m] + "." + bij[n][m+1:]
  return bij

r, c = IIS()
bij = [SI() for _ in range(r)]

for i in range(r):
  for j in range(c):
    if not bij[i][j] in {".", "#"}:
      bij = expload(bij=bij, i=i, j=j, r=r, c=c)
      bij[i] = bij[i][:j] + "." + bij[i][j+1:]

for i in range(r):
  print(bij[i])