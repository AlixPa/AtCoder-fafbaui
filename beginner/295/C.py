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

_ = II()
ls_a = LIIS()

dt_colors = dict()
for a in ls_a:
  if not a in dt_colors:
    dt_colors[a] = 0
  dt_colors[a] += 1

nb_pairs = 0
for color in dt_colors:
  nb_pairs += (dt_colors[color])//2

print(nb_pairs)