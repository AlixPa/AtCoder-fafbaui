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
ls_a = LIIS()

dt_a = dict()
for i in range(n):
  a = ls_a[i]
  if a in dt_a:
    dt_a[a].append(i)
  else:
    dt_a[a] = [i]

nb_tot = 0
for a in dt_a:
  len_a = len(dt_a[a])
  for i in range(len_a-1):
    nb_tot += (i+1)*(len_a - i - 1)*(dt_a[a][i+1] - dt_a[a][i] - 1)

print(nb_tot)