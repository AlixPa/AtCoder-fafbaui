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

MOD = 998244353
n = II()
ls_a = LIIS()

ls_a.sort()
full_sum_min = 0
nb_tot = 0
for i in range(1, n):
  full_sum_min *= 2
  full_sum_min += ls_a[i-1]
  full_sum_min %= MOD
  nb_tot += ls_a[i]*full_sum_min
  nb_tot %= MOD
for i in range(n):
  nb_tot += ls_a[i]*ls_a[i]
  nb_tot %= MOD

print(nb_tot)
