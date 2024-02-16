import sys, math
from collections import deque, defaultdict
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

n, x, y = IIS()
ls_a = LIIS()
x = x - ls_a[0]
ls_x = ls_a[2::2]
ls_y = ls_a[1::2]

def f(x0, ls):
  s = set()
  s.add(x0)
  for a in ls:
    tmp_s = set()
    for x_p in s:
      tmp_s.add(x_p + a)
      tmp_s.add(x_p - a)
    s = tmp_s
  return s

print("Yes" if (0 in f(x, ls_x) and 0 in f(y, ls_y)) else "No")