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

# Idea : Sum at each time the number of water used
# Table such that : if Si is start of use of new customer then table[Si] += Pi, if Ti is end then table[Ti] -= Pi

n, w = IIS()

ls_s = list()
ls_t = list()
for _ in range(n):
    s, t, p = IIS()
    ls_s.append([s, p])
    ls_t.append([t, p])
ls_s.sort()
ls_t.sort()

ls_use = [0 for _ in range(ls_t[-1][0] + 1)]

i_s = 0
while i_s < n and ls_s[i_s][0] == 0:
    ls_use[0] += ls_s[i_s][1]
    i_s += 1
i_t = 0
for i in range(1, ls_t[-1][0] + 1):
    ls_use[i] = ls_use[i-1]
    while i_s < n and ls_s[i_s][0] == i:
            ls_use[i] += ls_s[i_s][1]
            i_s += 1
    while i_t < n and ls_t[i_t][0] == i:
            ls_use[i] -= ls_t[i_t][1]
            i_t += 1

for u in ls_use:
    if u > w:
        print("No")
        sys.exit(0)
print("Yes")