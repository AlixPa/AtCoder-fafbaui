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

n, a, b = IIS()
s_tmp = SI()
s = [0 if c == "(" else 1 for c in s_tmp]

nb_open_tot = 0
for c in s:
  if c == 0:
    nb_open_tot += 1

if nb_open_tot > n:
  s = [(c+1)%2 for c in s]
  s = s[::-1]
  nb_open_tot = 2*n - nb_open_tot

i_first_too_closed = 0
nb_closed = 0
while i_first_too_closed < 2*n:
  if s[i_first_too_closed] == 0:
    nb_closed -= 1
  else:
    nb_closed += 1
  if nb_closed > 0:
    break
  i_first_too_closed += 1

i_first_too_open = 2*n - 1
nb_open = 0
while i_first_too_open >= 0:
  if s[i_first_too_open] == 0:
    nb_open += 1
  else:
    nb_open -= 1
  if nb_open > 0:
    break
  i_first_too_open -= 1

if i_first_too_closed == 2*n and i_first_too_open == -1:
  print(0)
  sys.exit(0)

cost = 0
while i_first_too_open >= 0:
  cost += min(a, 2*b)

  s[i_first_too_closed] = 0
  nb_closed -= 2
  i_first_too_closed += 1
  while i_first_too_closed < 2*n:
    if s[i_first_too_closed] == 0:
      nb_closed -= 1
    else:
      nb_closed += 1
    if nb_closed > 0:
      break
    i_first_too_closed += 1
  
  s[i_first_too_open] = 1
  nb_open -= 2
  i_first_too_open -= 1
  while i_first_too_open >= 0:
    if s[i_first_too_open] == 0:
      nb_open += 1
    else:
      nb_open -= 1
    if nb_open > 0:
      break
    i_first_too_open -= 1

cost += b*(n-nb_open_tot)
print(cost)