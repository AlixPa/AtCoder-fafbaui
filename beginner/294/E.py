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

L, n1, n2 = IIS()
ls_v1 = list()
ls_v2 = list()
for _ in range(n1):
  v, l = IIS()
  ls_v1.append((v, l))
for _ in range(n2):
  v, l = IIS()
  ls_v2.append((v, l))

i_1 = 0
i_2 = 0
nb_same = 0
while True:
  if i_1 >= n1 or i_2 >= n2:
    break
  v1, l1 = ls_v1[i_1]
  v2, l2 = ls_v2[i_2]
  if v1 == v2:
    if l1 <= l2:
      nb_same += l1
    else:
      nb_same += l2
  if l1 == l2:
    i_1 += 1
    i_2 += 1
  elif l1 < l2:
    i_1 += 1
    ls_v2[i_2] = (v2, l2-l1)
  else:
    i_2 += 1
    ls_v1[i_1] = (v1, l1-l2)

print(nb_same)