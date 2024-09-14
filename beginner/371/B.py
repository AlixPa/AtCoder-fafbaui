import sys, math, copy, itertools
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

n, m = IIS()
ls_fam = [True for _ in range(n+1)]
for _ in range(m):
    a, b = SIS()
    a = int(a)
    if ls_fam[a] and b == "M":
        ls_fam[a] = False
        print("Yes")
    else:
        print("No")