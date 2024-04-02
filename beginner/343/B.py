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

for _ in range(n):
  ls_neig = LIIS()
  ls_print = list()
  for i in range(n):
    if ls_neig[i] == 1:
      ls_print.append(i+1)
  print(*ls_print)