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

t = II()
for _ in range(t):
  n, a, b = IIS()
  if a > n:
    print("No")
    continue
  if b <= ((n+1)//2)*(n-a) - max(0, a - n//2)*(n-a):
    print("Yes")
  else:
    print("No")