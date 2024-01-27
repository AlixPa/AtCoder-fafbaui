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
s_out = ""

for e in s:
  if e == "0":
    s_out = s_out + "0"
  elif e == "1":
    s_out = s_out + "1"
  else:
    if len(s_out) > 0:
      s_out = s_out[:-1]

print(s_out)