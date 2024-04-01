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

x = SI()
if -10 < int(x) < 0:
  print(0)
  sys.exit(0)
elif int(x) == 0:
  print(0)
  sys.exit(0)
elif 0 < int(x) < 10:
  print(1)
  sys.exit(0)
nb = 0
if int(x[-1]) > 0 and x[0] != "-":
  nb += 1
y = x[:-1]
nb += int(y)

print(nb)