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

N, Q = IIS()
ls_balls = [i for i in range(N+1)]
dt_pos = dict()
for i in range(N):
  dt_pos[i+1] = i+1

for _ in range(Q):
  x = II()
  pos = dt_pos[x]
  save = ls_balls[pos]
  if pos == N:
    dt_pos[ls_balls[pos]] -= 1
    dt_pos[ls_balls[pos-1]] += 1
    ls_balls[pos] = ls_balls[pos-1]
    ls_balls[pos-1] = save
  else:
    dt_pos[ls_balls[pos]] += 1
    dt_pos[ls_balls[pos+1]] -= 1
    ls_balls[pos] = ls_balls[pos+1]
    ls_balls[pos+1] = save

print(*ls_balls[1:], sep=" ")