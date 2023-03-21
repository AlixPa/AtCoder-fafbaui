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

n, q = IIS()

smaller_not_come = 1
already_came = [False for _ in range(n+1)]

for _ in range(q):
  event = LIIS()
  if event[0] == 3:
    while already_came[smaller_not_come]:
      smaller_not_come += 1
    print(smaller_not_come)
  elif event[0] == 2:
    already_came[event[1]] = True
