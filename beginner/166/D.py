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

x = II()
a = 0
while True:
  obj = pow(a, 5) - x
  factor = 1
  if obj < 0:
    factor = -1
  b = 0
  while pow(b, 5) < abs(obj):
    b += 1
  if pow(b, 5) == abs(obj):
    print("%d %d"%(a, factor*b))
    sys.exit(0)
  a += 1