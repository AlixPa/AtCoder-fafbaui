import sys, math
from collections import deque, defaultdict
from heapq import heappop, heappush, heapify
def IIS(): return map(int, input().split())
def LIIS(): return list(IIS())
def SIIS(): return set(IIS())
def SIS(): return input().split()
def II(): return int(input())
def SI(): return input()
def FIS(): return map(float, input().split())
def FI(): return float(input())
sys.setrecursionlimit(10**8)

n, q = IIS()
ls_a = LIIS()
st_a = set(ls_a)

hq_free = [i for i in range(n+1) if i not in st_a]
heapify(hq_free)
dt_a = dict()
for a in ls_a:
  if a in dt_a:
    dt_a[a] += 1
  else:
    dt_a[a] = 1

for _ in range(q):
  i, x = IIS()
  prev = ls_a[i-1]
  ls_a[i-1] = x
  dt_a[prev] -= 1
  if x in dt_a:
    dt_a[x] += 1
  else:
    dt_a[x] = 1

  if dt_a[prev] == 0:
    heappush(hq_free, prev)
  
  mex = heappop(hq_free)
  while mex in dt_a and dt_a[mex] > 0:
    mex = heappop(hq_free)
  
  print(mex)
  heappush(hq_free, mex)