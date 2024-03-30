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

n, a, b = IIS()
ls_d = LIIS()

first_authorized_day = ls_d[0] - a + 1
last_authorized_day = ls_d[0]

for d in ls_d[1:]:
  shift_right = (d - first_authorized_day + 1)%(a+b)
  if shift_right > a:
    shift_right -= a
    first_authorized_day += shift_right
  shift_left = (d - last_authorized_day + 1)%(a+b)
  if shift_left > a:
    shift_left -= a
    last_authorized_day -= shift_left
  if first_authorized_day > last_authorized_day:
    print("No")
    sys.exit(0)
print("Yes")