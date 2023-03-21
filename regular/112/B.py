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

b, c = IIS()
if c == 1:
  if b == 0:
    print(1)
  else:
    print(2)
  sys.exit(0)

nb_possible = 0
c_tmp = c
if b < 0:
  c_tmp -= 1

nb_possible += 2*min(abs(b), 1 + (c_tmp-1)//2)

if 1 + c_tmp//2 > abs(b) or (c_tmp%2 == 0 and b != 0):
  nb_possible += 1

c_tmp = c
if b > 0:
  c_tmp -= 1

nb_possible += 2*((c_tmp-1)//2)

if c_tmp%2 == 0 and c > 2:
  nb_possible += 1

print(nb_possible)