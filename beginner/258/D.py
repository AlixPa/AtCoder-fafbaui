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

n, x = IIS()
ls_a = list()
ls_b = list()
for _ in range(n):
  a, b = IIS()
  ls_a.append(a)
  ls_b.append(b)

ls_cost = list()
cur = 0
for i in range(n):
  cur += ls_a[i] + ls_b[i]
  ls_cost.append(cur)

for i in range(min(x, n)):
  ls_cost[i] += (x-i-1)*ls_b[i]

print(min(ls_cost[:min(x,n)]))