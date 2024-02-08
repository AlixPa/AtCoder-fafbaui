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

n = II()
ls_cp = list()
ls_cp.append([])
for _ in range(n):
  ls_cp_i = LIIS()
  ls_cp.append(ls_cp_i)

already_read = [False for _ in range(n+1)]
list_order = list()

def condition_book(book):
  already_read[book] = True
  if ls_cp[book][0] != 0:
    for b in ls_cp[book][1:]:
      if not already_read[b]:
        condition_book(b)
  list_order.append(book)
  return 

condition_book(1)
print(*list_order[:-1])