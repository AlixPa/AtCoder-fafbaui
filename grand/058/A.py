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

n = II()
ls_p = LIIS()

ls_mooves = list()

for i in range(0, 2*n - 1, 2):
  if ls_p[i] > ls_p[i+1]:
    ls_p[i], ls_p[i+1] = ls_p[i+1], ls_p[i]
    ls_mooves.append(i+1)

for i in range(1, 2*n - 2, 2):
  if ls_p[i] < ls_p[i+1]:
    ls_p[i], ls_p[i+1] = ls_p[i+1], ls_p[i]
    ls_mooves.append(i+1)

print(len(ls_mooves))
print(*ls_mooves)