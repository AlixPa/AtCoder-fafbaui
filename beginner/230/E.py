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

n = II()
pow106 = pow(10, 6)

res = 0
for i in range(1, pow106+1):
  if i > n:
    print(res)
    sys.exit(0)
  res += n//i

nb_restant = n - pow106
i = 1
while nb_restant > 0:
  tmp = n//i - n//(i+1)
  tmp = min(tmp, nb_restant)
  nb_restant -= tmp
  res += i*tmp
  i += 1
print(res)