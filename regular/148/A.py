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

n = II()
ls_a = LIIS()

i = -1
ls_dif = list()
while i < n-1 and len(ls_dif) < 3:
  i += 1
  if ls_a[i] not in ls_dif:
    ls_dif.append(ls_a[i])

if len(ls_dif) == 1:
  print(1)
  sys.exit(0)
elif len(ls_dif) == 2:
  if abs(ls_dif[0] - ls_dif[1]) == 1:
    print(2)
  else:
    print(1)
  sys.exit(0)

prev_gcd = math.gcd(ls_dif[1]-ls_dif[0], ls_dif[2]-ls_dif[1])
i -= 1
while i < n-2:
  i += 1
  if ls_a[i] == ls_a[i+1]:
    continue
  prev_gcd = math.gcd(prev_gcd, ls_a[i]-ls_a[i+1])
  if prev_gcd == 1:
    break

if prev_gcd > 1:
  print(1)
else:
  print(2)