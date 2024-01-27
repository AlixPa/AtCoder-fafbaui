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

n = II()
ls_v = LIIS()

dt_v_even = dict()
dt_v_odd = dict()
for v in ls_v[::2]:
  if v in dt_v_even:
    dt_v_even[v] += 1
  else:
    dt_v_even[v] = 1
for v in ls_v[1::2]:
  if v in dt_v_odd:
    dt_v_odd[v] += 1
  else:
    dt_v_odd[v] = 1

max1_even = max(dt_v_even, key=dt_v_even.get)
max1_even_nb = dt_v_even[max1_even]
dt_v_even[max1_even] = 0
max2_even = max(dt_v_even, key=dt_v_even.get)
max2_even_nb = dt_v_even[max2_even]
dt_v_even[max2_even] = 0
max1_odd = max(dt_v_odd, key=dt_v_odd.get)
max1_odd_nb = dt_v_odd[max1_odd]
dt_v_odd[max1_odd] = 0
max2_odd = max(dt_v_odd, key=dt_v_odd.get)
max2_odd_nb = dt_v_odd[max2_odd]
dt_v_odd[max2_odd] = 0

if max1_even != max1_odd:
  print(n - (max1_even_nb + max1_odd_nb))
else:
  print(n - max(max1_even_nb + max2_odd_nb, max2_even_nb + max1_odd_nb))