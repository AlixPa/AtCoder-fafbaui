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
nb_ab = 0
nb_a = 0
nb_b = 0
count = 0
for _ in range(n):
  s = SI()
  e_prev = s[0]
  for e in s[1:]:
    if e_prev == "A" and e == "B":
      count += 1
    e_prev = e
  if s[0] == "B" and s[-1] == "A":
    nb_ab += 1
  elif s[0] == "B":
    nb_b += 1
  elif s[-1] == "A":
    nb_a += 1

count += max(nb_ab-1, 0)
if nb_b != 0 or nb_a != 0:
  count += min(nb_a, nb_b)
  if nb_ab > 0:
    count += 1

print(count)