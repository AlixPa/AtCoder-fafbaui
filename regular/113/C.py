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

S = SI()
N = len(S)
if N <= 2:
  print(0)
  sys.exit(0)
dt_letters = dict()
for i in range(ord("a"), ord("z")+1):
  dt_letters[chr(i)] = 0
cpt = 0

letter = S[-1]
for i in range(N-2, 0, -1):
  dt_letters[S[i+1]] += 1
  if S[i] == letter:
    continue
  letter = S[i]
  if S[i] == S[i-1]:
    cpt += (N-1) - i - dt_letters[S[i]]
    for j in range(ord("a"), ord("z")+1):
      dt_letters[chr(j)] = 0
    dt_letters[S[i]] = (N-1) - i

print(cpt)