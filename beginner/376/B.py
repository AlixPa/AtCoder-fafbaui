import sys, math, copy, itertools
from bisect import insort, insort_left, insort_right
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

n, q = IIS()
dt_hands = {"L": 1, "R": 2}
dt_inv = {"L": "R", "R": "L"}
nb_move = 0

for _ in range(q):
  h, t = SIS()
  t = int(t)
  if abs(t - dt_hands[h]) <= n//2:
    if min(t, dt_hands[h]) < dt_hands[dt_inv[h]] < max(t, dt_hands[h]):
      nb_move += n - abs(t - dt_hands[h])
    else:
      nb_move += abs(t - dt_hands[h])
  else:
    if max(t, dt_hands[h]) < dt_hands[dt_inv[h]] or dt_hands[dt_inv[h]] < min(t, dt_hands[h]):
      nb_move += abs(t - dt_hands[h])
    else:
      nb_move += n - abs(t - dt_hands[h])
  dt_hands[h] = t

print(nb_move)
