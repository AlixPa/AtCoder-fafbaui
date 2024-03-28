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
ls_a = list()
for _ in range(n):
  a = II()
  ls_a.append(a)

if ls_a[0] > 0:
  print(-1)
  sys.exit(0)

for i in range(1, n):
  if ls_a[i] > ls_a[i-1] + 1:
    print(-1)
    sys.exit(0)

res = 0
for i in range(n-1):
  if ls_a[i] != ls_a[i+1] - 1:
    res += ls_a[i]
res += ls_a[-1]

print(res)