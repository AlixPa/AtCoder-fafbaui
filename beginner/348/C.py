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
dt_b = dict()
for _ in range(n):
  a, c = IIS()
  if c not in dt_b:
    dt_b[c] = math.inf
  if a < dt_b[c]:
    dt_b[c] = a
ls_b = list()
for c in dt_b:
  ls_b.append(dt_b[c])
print(max(ls_b))