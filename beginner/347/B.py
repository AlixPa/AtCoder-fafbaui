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

s = SI()

nb = 0
for i in range(1, len(s)+1):
  st_dif = set()
  for j in range(len(s)-i+1):
    st_dif.add(s[j:j+i])
  nb += len(st_dif)
print(nb)