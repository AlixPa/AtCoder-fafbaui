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

def addToSorted(ls, e):
  left = 0
  right = len(ls)
  while left < right:
    center = left + (right - left)//2
    if ls[center] < e:
      left = center + 1
    else:
      right = center
  ls.insert(left, e)
  return ls

q = II()
s = list()
s_dt = dict()
for _ in range(q):
  ls_i = LIIS()
  if len(ls_i) == 1:
    print(s[-1] - s[0])
  elif len(ls_i) == 2:
    if ls_i[1] in s_dt:
      s_dt[ls_i[1]] += 1
    else:
      s_dt[ls_i[1]] = 1
    if s_dt[ls_i[1]] == 1:
      s = addToSorted(s, ls_i[1])
  else :
    if ls_i[1] not in s_dt:
      continue
    nb_in = s_dt[ls_i[1]]
    nb_sup = min(ls_i[2], nb_in)
    if nb_sup == nb_in:
      s.remove(ls_i[1])
    s_dt[ls_i[1]] -= nb_sup