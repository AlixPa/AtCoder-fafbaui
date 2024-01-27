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

N, T = IIS()
ls_t = LIIS()

tot_time = T
for i in range(1, N):
  dif_time = ls_t[i] - ls_t[i-1]
  if dif_time >= T :
    tot_time += T
  else:
    tot_time += dif_time
print(tot_time)