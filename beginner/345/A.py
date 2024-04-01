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

s = SI()
if s[0] != "<" or s[-1] != ">":
  print("No")
  sys.exit(0)
for c in s[1:-1]:
  if c != "=":
    print("No")
    sys.exit(0)
print("Yes")