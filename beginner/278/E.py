import sys, math, copy, itertools
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

def init(mat_a, dt_nb, k, h, w):
  nb = len(dt_nb)
  new_dt = copy.deepcopy(dt_nb)
  for i in range(k, k+h):
    for j in range(w):
      new_dt[mat_a[i][j]] -= 1
      if new_dt[mat_a[i][j]] == 0:
        nb -= 1
  return new_dt, nb

H, W, N, h, w = IIS()
mat_a = list()
for _ in range(H):
  ls_a = LIIS()
  mat_a.append(ls_a)

dt_nb = dict()
for i in range(H):
  for j in range(W):
    if mat_a[i][j] not in dt_nb:
      dt_nb[mat_a[i][j]] = 0
    dt_nb[mat_a[i][j]] += 1

mat_res = [[0 for _ in range(W-w+1)] for _ in range(H-h+1)]
for k in range(H-h+1):
  dt_init, nb_init = init(mat_a, dt_nb, k, h, w)
  mat_res[k][0] = nb_init
  for l in range(W-w):
    # add la colonne l
    for i in range(h):
      if dt_init[mat_a[k+i][l]] == 0:
        nb_init += 1
      dt_init[mat_a[k+i][l]] += 1
    # suppr la colonne l+w
    for i in range(h):
      dt_init[mat_a[k+i][l+w]] -= 1
      if dt_init[mat_a[k+i][l+w]] == 0:
        nb_init -= 1
    mat_res[k][l+1] = nb_init

for i in range(H-h+1):
  print(*mat_res[i])