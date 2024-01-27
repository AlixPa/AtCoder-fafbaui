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

N = II()
s = SI()
t = SI()

for i in range(N):
  can_chevaucher = True
  for j in range(N - i):
    if s[i + j] != t[j]:
      can_chevaucher = False
  if can_chevaucher:
    print(N + i)
    sys.exit(0)
print(2*N)