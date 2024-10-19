import sys, math, copy, itertools
from bisect import insort, insort_left, insort_right
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

_, c = IIS()
ls_t = LIIS()

nb_candy = 0
last_time = -math.inf
for t in ls_t:
  if t - last_time >= c:
    nb_candy += 1
    last_time = t

print(nb_candy)