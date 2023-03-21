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

n, m = IIS()
ls_a = LIIS()
ls_b = LIIS()

print_a = list()
print_b = list()
i_a = 0
i_b = 0

for i in range(n+m):
  if i_a >= len(ls_a):
    print_b += [k for k in range(i+1, n+m+1)]
    break
  if i_b >= len(ls_b):
    print_a += [k for k in range(i+1, n+m+1)]
    break
  if ls_a[i_a] < ls_b[i_b]:
    i_a += 1
    print_a.append(i+1)
  else:
    i_b += 1
    print_b.append(i+1)

print(*print_a)
print(*print_b)