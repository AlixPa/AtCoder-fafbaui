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

N, K, L = IIS()
MOD = 998244353

nb = 1
for i in range(N-K+1):
  nb *= (L - i)
  nb %= MOD
  if nb == 0:
    nb += MOD
for _ in range(K-1):
  nb *= (L-N+K)
  nb %= MOD
  if nb == 0:
    nb += MOD
print(nb%MOD)