import sys, math
from collections import deque
def IIS(): return map(int, input().split())
def SIS(): return input().split()
def II(): return int(input())
def SI(): return input()
def FIS(): return map(float, input().split())
def FI(): return float(input())
sys.setrecursionlimit(10**8)

x, y, a, b, c = IIS()
ls_A = list(IIS())
ls_B = list(IIS())
ls_C = list(IIS())

ls_A.sort()
ls_B.sort()
ls_C.sort()
lenA = len(ls_A)
lenB = len(ls_B)
lenC = len(ls_C)

rest_sum = x + y
sum_pqr = 0
for _ in range(rest_sum):
  maxA = 0
  maxB = 0
  maxC = 0
  if lenA > 0:
    maxA = ls_A[-1]
  if lenB > 0:
    maxB = ls_B[-1]
  if lenC > 0:
    maxC = ls_C[-1]
  maxABC = max(maxA, maxB, maxC)
  maxAC = max(maxA, maxC)
  maxBC = max(maxB, maxC)
  removeA = False
  removeB = False
  if maxA == maxABC:
    if x > 0:
      removeA = True
    else:
      if maxB == maxBC:
        removeB = True
  elif maxB == maxABC:
    if y > 0:
      removeB = True
    else:
      if maxA == maxAC:
        removeA = True
    
  if removeA:
    x -= 1
    ls_A.pop(-1)
    lenA -= 1
    sum_pqr += maxA
  elif removeB:
    y -= 1
    ls_B.pop(-1)
    lenB -= 1
    sum_pqr += maxB
  else:
    ls_C.pop(-1)
    lenC -= 1
    sum_pqr += maxC



print(sum_pqr)