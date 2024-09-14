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

def dichoSearch(k, ls):
  '''
  Take a sorted listed and an item, return the indice of the greater smaller int of the item (-1 if the item is smaller than all)
  (3, [1, 4, 7]) => 0
  (5, [0, 1, 2, 3, 10]) => 3
  '''
  if k < ls[0]:
    return -1
  left = 0
  right = len(ls) - 1
  while True:
    dif = right - left
    if dif == 0:
      return left
    center = left + (dif+1)//2
    if ls[center] <= k:
      left = center
    else:
      right = center - 1

n = II()

ls_x = LIIS()
ls_p = LIIS()

sum_vil = [0 for _ in range(n+2)]
for i in range(1, n+1):
    sum_vil[i] = sum_vil[i-1] + ls_p[i-1]

q = II()
for _ in range(q):
  l, r = IIS()
  i_l = dichoSearch(l, ls_x)
  i_r = dichoSearch(r, ls_x)
  if l > ls_x[i_l]:
    i_l += 1
  if r < ls_x[i_r]:
    i_r -= 1
  i_l += 1
  i_r += 1
  print(sum_vil[i_r] - sum_vil[i_l-1])