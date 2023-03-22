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

n, k = IIS()

if k == 0:
  print(n*n)
  sys.exit(0)

nb_pairs = 0
for b in range(k+1, n+1):
  for a in range(k, n+1, b):
    nb_pairs += min(b-k, n-a+1)
  
print(nb_pairs)