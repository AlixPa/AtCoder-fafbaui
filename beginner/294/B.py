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

h, w = IIS()
mat_a = list()
for _ in range(h):
  ls_a = LIIS()
  mat_a.append(ls_a)
ls_s = list()
for ls_a in mat_a:
  s = ""
  for a in ls_a:
    if a == 0:
      s += "."
    else:
      s += chr(ord("A") + a - 1)
  ls_s.append(s)
for s in ls_s:
  print(s)