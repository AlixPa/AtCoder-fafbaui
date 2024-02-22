import sys, math
from collections import deque, defaultdict
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
ls_test = list()
for i in range(n):
  a = II()
  ls_t = list()
  for _ in range(a):
    x, y = IIS()
    ls_t.append((x, y))
  ls_test.append(ls_t)
pow2n = pow(2, n)
nb_max = 0
for i in range(1, pow2n):
  ls_trust = [True if ((pow2n - i)//pow(2, j))%2 == 1 else False for j in range(n)]
  good = True
  for j in range(n):
    if ls_trust[j]:
      for x,y in ls_test[j]:
        if (y == 1 and not ls_trust[x - 1]) or (y == 0 and ls_trust[x - 1]):
          good = False
          break
    if not good:
      break
  if good:
    tmp = 0
    for p in ls_trust:
      if p:
        tmp += 1
    nb_max = max(nb_max, tmp)
print(nb_max)
      
  
