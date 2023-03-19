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

def dijkstraSpe(ls_vertices, x, y, is_out, time_travel):
  heap = list()
  heappush(heap, (time_travel[x], x))
  while heap:
    current_time, city = heappop(heap)
    if city == y:
      return current_time
    if is_out[city]:
      continue
    for next_city in ls_vertices[city]:
      if not is_out[next_city]:
        min_arrival = math.inf
        for (t, k) in ls_vertices[city][next_city]:
          tmp_arrival = current_time + t + (k - (current_time%k))%k
          if tmp_arrival < min_arrival:
            min_arrival = tmp_arrival
        if min_arrival < time_travel[next_city]:
          time_travel[next_city] = min_arrival
          heappush(heap, (min_arrival, next_city))
    is_out[city] = True
  return -1

n, m, x, y = IIS()

ls_vertices = [dict() for _ in range(n+1)]
for _ in range(m):
  a, b, t, k = IIS()
  if a not in ls_vertices[b]:
    ls_vertices[a][b] = set()
    ls_vertices[b][a] = set()
  ls_vertices[a][b].add((t,k))
  ls_vertices[b][a].add((t,k))

is_out = [False for _ in range(n+1)]
time_travel = [math.inf for _ in range(n+1)]
time_travel[x] = 0

print(dijkstraSpe(ls_vertices=ls_vertices, x=x, y=y, is_out=is_out, time_travel=time_travel))