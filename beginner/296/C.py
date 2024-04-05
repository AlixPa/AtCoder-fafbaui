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

n, x = IIS()
ls_a = LIIS()

dt_ajx = dict()
for a in ls_a:
  dt_ajx[a+x] = 0
for a in ls_a:
  if a in dt_ajx:
    print("Yes")
    sys.exit(0)
print("No")