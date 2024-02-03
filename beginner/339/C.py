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
ls_a = LIIS()

nb_pass = 0
min_pass = 0
for i in range(n):
  nb_pass += ls_a[i]
  if nb_pass < min_pass:
    min_pass = nb_pass
nb_pass -= min_pass

print(nb_pass)
