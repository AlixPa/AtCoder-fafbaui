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

h, w, m = IIS()
ls_tmp_tax = list()
for _ in range(m):
  t, a, x = IIS()
  ls_tmp_tax.append([t, a, x])

st_ta = set()
ls_tax = list()
for e in ls_tmp_tax[::-1]:
  if (e[0], e[1]) not in st_ta:
    st_ta.add((e[0], e[1]))
    ls_tax.append(e)

nb_col_paint = 0
nb_row_paint = 0
dt_paint = dict()
for e in ls_tax:
  if e[2] not in dt_paint:
    dt_paint[e[2]] = 0
  if e[0] == 1:
    dt_paint[e[2]] += w - nb_col_paint
    nb_row_paint += 1
  else:
    dt_paint[e[2]] += h - nb_row_paint
    nb_col_paint += 1

if 0 not in dt_paint:
  dt_paint[0] = 0
sum_c = 0
for c in dt_paint:
  sum_c += dt_paint[c]
dt_paint[0] += (h*w) - sum_c

ls_col = list()
for c in dt_paint:
  if dt_paint[c] > 0:
    ls_col.append([c, dt_paint[c]])
ls_col.sort()

print(len(ls_col))
for e in ls_col:
  print(*e)
