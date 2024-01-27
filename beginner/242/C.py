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

N = II()
MOD = 998244353

ls_n = [1 for _ in range(10)]

for _ in range(N - 1):
  ls_n_save = [e%MOD for e in ls_n]
  ls_n[1] = ls_n_save[1] + ls_n_save[2]
  ls_n[9] = ls_n_save[8] + ls_n_save[9]
  for i in range(2, 9):
    ls_n[i] = ls_n_save[i-1] + ls_n_save[i] + ls_n_save[i+1]

sm = 0
for e in ls_n[1:]:
  sm += e
  sm %= MOD
print(sm)