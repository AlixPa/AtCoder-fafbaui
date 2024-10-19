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

#Complexity oof because of list creation on some instances. Better with a shift index
n = II()
ls_a = LIIS()
ls_b = LIIS()

ls_a.sort(reverse = True)
ls_b.sort(reverse = True)
box_purchased = 0

for i in range(n):
  if i == len(ls_b):
    box_purchased = ls_a[i]
    ls_b.append(0)
  elif ls_b[i] < ls_a[i]:
    box_purchased = ls_a[i]
    ls_b = ls_b[:i] + [0] + ls_b[i:]
if len(ls_b) == n:
  print(box_purchased)
else:
  print(-1)
    