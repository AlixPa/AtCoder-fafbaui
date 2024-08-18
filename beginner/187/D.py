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

n = II()
ls_a = list()
ls_b = list()
for _ in range(n):
    a, b = IIS()
    ls_a.append(a)
    ls_b.append(b)
ls_dif = list()
for i in range(n):
    ls_dif.append([2*ls_a[i]+ls_b[i], i])
ls_dif.sort(reverse = True)

votes_taka = 0
i = 0
j = n-1
while i <= j:
    if votes_taka - ls_a[ls_dif[j][1]] > 0:
        votes_taka -= ls_a[ls_dif[j][1]]
        j -= 1
    else:
        votes_taka += ls_a[ls_dif[i][1]] + ls_b[ls_dif[i][1]]
        i += 1

print(i)