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

n, m, k = IIS()

left = 0
right = max(n*k*4, m*k*4)
diviser = (n*m)//math.gcd(n,m)
while True:
  center = (left+right)//2
  nb_k = center//n + center//m - 2*(center//diviser)
  if nb_k == k:
    if (center%n == 0 or center%m == 0) and (center%n != 0 or center%m != 0):
      print(center)
      sys.exit(0)
    else:
      right = center
  elif nb_k < k:
    left = center
  else:
    right = center