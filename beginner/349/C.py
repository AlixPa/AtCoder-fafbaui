import sys, math, copy, itertools
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

s = SI()
t = SI()
t = t.lower()

i = 0
for c in s:
  if i > 2:
    print("Yes")
    sys.exit(0)
  if c == t[i]:
    i += 1

if i == 3 or (i == 2 and t[i] == "x"):
  print("Yes")
else:
  print("No")