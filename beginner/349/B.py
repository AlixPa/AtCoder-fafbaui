import sys, math, copy, itertools
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

s = SI()

dt_c = dict()
for i in range(ord("a"), ord("z") + 1):
  dt_c[chr(i)] = 0
for c in s:
  dt_c[c] += 1
for i in range(len(s)):
  nb = 0
  for c in dt_c:
    if dt_c[c] == i+1:
      nb += 1
  if nb != 0 and nb != 2:
    print("No")
    sys.exit(0)
print("Yes")