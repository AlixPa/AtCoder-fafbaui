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

s = SI()

if s[0] in [chr(e) for e in range(ord("A"), ord("Z") + 1)]:
  for l in s[1:]:
    if l not in [chr(e) for e in range(ord("a"), ord("z") + 1)]:
      print("No")
      sys.exit(0)
  print("Yes")
  sys.exit(0)
print("No")