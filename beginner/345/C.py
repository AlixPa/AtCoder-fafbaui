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

s = SI()

dt_l = dict()
for c in s:
  if c in dt_l:
    dt_l[c] += 1
  else:
    dt_l[c] = 1

nb = len(s)*(len(s)-1)//2
for c in dt_l:
  nb -= dt_l[c]*(dt_l[c]-1)//2

for c in dt_l:
  if dt_l[c] > 1:
    nb += 1
    break

print(nb)