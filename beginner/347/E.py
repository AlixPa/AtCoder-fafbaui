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

n, q = IIS()
ls_x_tmp = LIIS()
ls_x = [x-1 for x in ls_x_tmp]

st_s = {ls_x[0]}
sum_q = [1 for _ in range(q+1)]
sum_q[0] = 0
len_s = 1
for i in range(1, q):
  if ls_x[i] in st_s:
    len_s -= 1
    st_s.remove(ls_x[i])
  else:
    len_s += 1
    st_s.add(ls_x[i])
  sum_q[i+1] = sum_q[i] + len_s

join_a = [-1 for i in range(n)]
ls_a = [0 for _ in range(n)]

st_s = set()
for i in range(q):
  if ls_x[i] in st_s:
    ls_a[ls_x[i]] += sum_q[i] - sum_q[join_a[ls_x[i]]]
    st_s.remove(ls_x[i])
  else:
    st_s.add(ls_x[i])
    join_a[ls_x[i]] = i

for a in st_s:
  ls_a[a] += sum_q[-1] - sum_q[join_a[a]]

print(*ls_a)