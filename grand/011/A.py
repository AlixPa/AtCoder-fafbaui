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

N, C, K = IIS()
ls_pass = list()
for _ in range(N):
  ls_pass.append(II())
ls_pass.sort()

nb_bus = 1
pass_bus = 1
dep_bus = ls_pass[-1]
for t in ls_pass[::-1][1:]:
  if pass_bus < C and dep_bus-t <= K:
    pass_bus += 1
  else:
    nb_bus += 1
    pass_bus = 1
    dep_bus = t

print(nb_bus)