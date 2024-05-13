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

n = II()
t = SI()

if n == 1:
  if t == "1":
    print(2*pow(10, 10))
  else:
    print(pow(10, 10))
  sys.exit(0)
elif n == 2:
  if t == "11" or t == "10":
    print(pow(10, 10))
  elif t == "01":
    print(pow(10, 10) - 1)
  else:
    print(0)
  sys.exit(0)

shift = -1
if t[:3] == "110":
  shift = 0
elif t[:3] == "101":
  shift = 1
elif t[:3] == "011":
  shift = 2
else:
  print(0)
  sys.exit(0)

verif = "110"
for i in range(n):
  if t[i] != verif[(i+shift)%3]:
    print(0)
    sys.exit(0)

nb_used = (n+shift)//3
if (n+shift)%3 != 0:
  nb_used += 1

print(pow(10, 10) - nb_used + 1)