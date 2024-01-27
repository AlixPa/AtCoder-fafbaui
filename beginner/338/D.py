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

N, M = IIS()
ls_x = LIIS()
ls_x = [e-1 for e in ls_x]

ls_sum_bridges = [0 for _ in range(N)]

x_prev = ls_x[0]
dist_tot = 0
for x in ls_x[1:]:
  dist = abs(x_prev - x)
  shortest_dist = min(dist, N-dist)
  longest_distance = max(dist, N-dist)
  dist_tot += shortest_dist
  if shortest_dist == longest_distance:
    x_prev = x
    continue
  dist_add = longest_distance - shortest_dist
  if dist == shortest_dist:
    ls_sum_bridges[min(x_prev, x)] += dist_add
    ls_sum_bridges[max(x_prev, x)] -= dist_add
  else:
    ls_sum_bridges[max(x_prev, x)] += dist_add
    ls_sum_bridges[0] += dist_add
    ls_sum_bridges[min(x_prev, x)] -= dist_add
  x_prev = x

sum_cur = ls_sum_bridges[0]
sum_min = sum_cur
for i in range(1, N):
  sum_cur += ls_sum_bridges[i]
  if sum_cur < sum_min:
    sum_min = sum_cur
print(dist_tot + sum_min)