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

N = II()
ls_q = LIIS()
ls_a = LIIS()
ls_b = LIIS()

max_nb_a = pow(10, 6) + 1
for i in range(N):
  if ls_a[i] > 0:
    max_nb_a = min(max_nb_a, ls_q[i]//ls_a[i])

ls_q_rest = [(ls_q[i] - max_nb_a*ls_a[i]) for i in range(N)]
nb_a = max_nb_a
nb_b = 0
while(True):
  cant_no_more = False
  for i in range(N):
    if ls_q_rest[i] < ls_b[i]:
      cant_no_more = True
  if cant_no_more:
    break
  nb_b += 1
  for i in range(N):
    ls_q_rest[i] -= ls_b[i]
nb_before = nb_a + nb_b
while(True):
  if nb_a == 0:
    break
  nb_a -= 1
  for i in range(N):
    ls_q_rest[i] += ls_a[i]
  while(True):
    cant_no_more = False
    for i in range(N):
      if ls_q_rest[i] < ls_b[i]:
        cant_no_more = True
    if cant_no_more:
      break
    nb_b += 1
    for i in range(N):
      ls_q_rest[i] -= ls_b[i]
  if nb_before > nb_a + nb_b:
    break
  nb_before = nb_a + nb_b

print(nb_before)