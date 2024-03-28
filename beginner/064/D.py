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

n = II()
s = SI()

nb_open = 0
nb_closed = 0
nb_open_needed = 0

for c in s:
  if c == ")":
    nb_closed += 1
  else:
    if nb_closed > 0:
      nb_open_needed += nb_closed
      nb_closed = 0
    nb_closed -= 1

if nb_closed > 0:
  nb_open_needed += nb_closed

s = "("*nb_open_needed + s
if nb_closed < 0:
  s = s + ")"*(-nb_closed)

print(s)