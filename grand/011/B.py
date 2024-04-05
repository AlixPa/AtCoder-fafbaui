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

n = II()
ls_a = LIIS()

ls_crea = [(ls_a[c], c+1) for c in range(n)]
ls_crea.sort()
ls_sum = list()

cur = 0
for s, _ in ls_crea:
  cur += s
  ls_sum.append(cur)

nb = 0
for i in range(n-1):
  s, _ = ls_crea[i+1]
  if 2*ls_sum[i] < s:
    nb = 0
  else:
    nb += 1

print(nb+1)