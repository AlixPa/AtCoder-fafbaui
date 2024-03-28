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

n = II()
ls_a = LIIS()
MOD = 998244353

ls10 = [0 for _ in range(10)]
ls10[(ls_a[0]+ls_a[1])%10] += 1
ls10[(ls_a[0]*ls_a[1])%10] += 1

for a in ls_a[2:]:
  tmp = [0 for c in ls10]
  for i in range(10):
    tmp[(i+a)%10] += ls10[i]
    tmp[(i*a)%10] += ls10[i]
  ls10 = tmp
  for i in range(10):
    ls10[i] %= 998244353

for c in ls10:
  print(c)