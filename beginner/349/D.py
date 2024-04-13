import sys, math, copy, itertools
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

def mon_ceil(n, q):
  if n%q == 0:
    return n//q
  else:
    return (n//q) + 1

def getBiggest(l, r):
  if l == r:
    return [] 
  dif = r - l
  max_pow = int(math.log2(dif))
  while True:
    dpi = pow(2, max_pow)
    if (mon_ceil(l, dpi) + 1)*dpi <= r:
      break
    max_pow -= 1
  dpi = pow(2, max_pow)
  ls = [mon_ceil(l, dpi)*dpi, (mon_ceil(l, dpi) + 1)*dpi]
  return getBiggest(l, mon_ceil(l, dpi)*dpi) + ls + getBiggest((mon_ceil(l, dpi) + 1)*dpi, r)

l, r = IIS()
ls = getBiggest(l, r)
print(len(ls)//2)
for i in range(len(ls)//2):
  print("%d %d"%(ls[2*i], ls[2*i+1]))