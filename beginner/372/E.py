import sys, math, copy, itertools, bisect
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

ls_edges = [[[i+1], {i+1}] for i in range(n)]

for _ in range(q):
  a, b, c = IIS()
  if a == 1:
    if ls_edges[b-1] is ls_edges[c-1]:
      continue
    biggest_vert = c-1
    smallest_vert = b-1
    if len(ls_edges[b-1][0]) > len(ls_edges[c-1][0]):
      biggest_vert = b-1
      smallest_vert = c-1
    for v in ls_edges[smallest_vert][0]:
      if v not in ls_edges[biggest_vert][1]:
        if v-1 != smallest_vert:
            ls_edges[v-1] = ls_edges[biggest_vert]
        bisect.insort(ls_edges[biggest_vert][0], v)
        ls_edges[biggest_vert][1].add(v)
    ls_edges[smallest_vert] = ls_edges[biggest_vert]
  else:
    if len(ls_edges[b-1][0]) < c:
      print(-1)
    else:
      print(ls_edges[b-1][0][-c])