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

n, t = IIS()

dt_scores = dict()
dt_scores[0] = n
ls_scores = [0]*n
nb_diff = 1

for _ in range(t):
  a, b = IIS()
  prev_score = ls_scores[a-1]
  ls_scores[a-1] += b
  new_score = ls_scores[a-1]
  dt_scores[prev_score] -= 1
  if dt_scores[prev_score] == 0:
    nb_diff -= 1
  if new_score not in dt_scores:
    dt_scores[new_score] = 0
  dt_scores[new_score] += 1
  if dt_scores[new_score] == 1:
    nb_diff += 1
  print(nb_diff)