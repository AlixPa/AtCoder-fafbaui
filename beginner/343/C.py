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

def verifPalyn(k):
  sk = str(k)
  for i in range(math.ceil(len(sk)/2)):
    if sk[i] != sk[-(i+1)]:
      return False
  return True

for k in range(math.floor(pow(n, 1/3)) + 1, 0, -1):
  if verifPalyn(pow(k, 3)) and pow(k,3) <= n:
    print(pow(k, 3))
    sys.exit(0)
