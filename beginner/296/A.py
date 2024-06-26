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
s = SI()

if len(s) == 0:
  print("Yes")
  sys.exit(0)

prev = s[0]
for c in s[1:]:
  if c == prev:
    print("No")
    sys.exit(0)
  prev = c
print("Yes")