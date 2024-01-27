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

dt_c = dict()
for e in [chr(l) for l in range(ord("a"), ord("z") + 1)]:
  dt_c[e] = 0

for e in s:
  dt_c[e] += 1

max_elem = max(dt_c, key=dt_c.get)
nb_max = dt_c[max_elem]
max_elems = list()
for e in dt_c:
  if dt_c[e] == nb_max:
    max_elems.append(e)
max_elems.sort()
print(max_elems[0])