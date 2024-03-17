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
ls_c = SI()

sm = 1
ls_sum = [1]
for c in ls_c[1:]:
  if c == ls_c[0]:
    sm += 1
  else:
    sm -= 1
  ls_sum.append(sm)

nb_dif = 1
for i in range(n-1):
  if ls_c[i+1] != ls_c[0] and ls_sum[i] in {0, 1, 2}:
    nb_dif += 1

print(nb_dif)
