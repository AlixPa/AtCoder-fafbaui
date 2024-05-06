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
pn = LIIS()

nb = 0

if pn[-1] == n:
  pn[-1] = pn[-2]
  pn[-2] = n
  nb += 1
if pn[0] == 1:
  pn[0] = pn[1]
  pn[1] = 0
  nb += 1

for i in range(1, n-1):
  if pn[i] == i+1:
    pn[i] = pn[i+1]
    pn[i+1] = i+1
    nb += 1

print(nb)

