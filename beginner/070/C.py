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

n = II()
ls_clocks = list()
for _ in range(n):
  t = II()
  ls_clocks.append(t)

lcm = ls_clocks[0]
for t in ls_clocks[1:]:
  lcm = math.lcm(lcm, t)
print(lcm)