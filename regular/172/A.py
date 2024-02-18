import sys, math
from collections import deque, defaultdict
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

H, W, N = IIS()
ls_a = LIIS()

dt_a = dict()
for i in range(26):
  dt_a[i] = 0
for a in ls_a:
  dt_a[a] += 1

def f(x, y):
  if x > y:
    tmp = x
    x = y
    y = tmp
  nb_max = 0
  pow_cur = 0
  for i in range(26):
    nb_square = dt_a[25-i]
    pow_cur = pow(2, 25-i)
    if nb_square == 0 or x < pow_cur:
      continue
    nb_max = min(nb_square, y//pow_cur)
    dt_a[25-i] -= nb_max
    break
  if nb_max > 0:
    f(x-pow_cur, pow_cur*nb_max)
    f(x, y-pow_cur*nb_max)
  return

f(H, W)

for a in dt_a:
  if dt_a[a] > 0:
    print("No")
    sys.exit(0)
print("Yes")