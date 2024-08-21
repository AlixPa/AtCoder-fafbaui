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

# Idea :
# Coming from left to right, each waal must be destoy, so the wall with the earliest ending should be punch too
# If the first stop wall stops at column C, we can puch on [C, C+D-1], destroy all walls on the interval, and iterate until no more walls

n, d = IIS()

ls_l = list()
ls_r = list()
for i in range(n):
    l, r = IIS()
    ls_l.append([l, i])
    ls_r.append([r, i])
ls_l.sort()
ls_r.sort()

ls_destroyed = [False for _ in range(n)]

i_r = 0
i_l = 0
nb_punch = 0
while i_r < n:
    nb_punch += 1
    # Destroy from this index
    while i_l < n and ls_l[i_l][0] < ls_r[i_r][0]+d:
        ls_destroyed[ls_l[i_l][1]] = True
        i_l += 1
    while i_r < n and ls_destroyed[ls_r[i_r][1]]:
        i_r += 1

print(nb_punch)