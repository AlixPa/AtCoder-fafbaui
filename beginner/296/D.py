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

n, m = IIS()

res = math.inf
for a in range(1, math.ceil(pow(m, 0.5))+1):
  b = math.ceil(m/a)
  if b > n or a > n:
    continue
  res = min(res, a*b)
if res != math.inf:
  print(res)
else:
  print(-1)