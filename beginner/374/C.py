import sys, math, copy, itertools
from bisect import insort, insort_left, insort_right
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
ls_k = LIIS()

half_k = sum(ls_k)/2
min_dist_half = math.inf
max_min = 0


for i in range(pow(2, n)):
    cur_sum = 0
    for j in range(n):
        if (i//pow(2,j))%2 == 1:
            cur_sum += ls_k[j]
    if cur_sum < half_k:
        continue
    if min_dist_half > cur_sum-half_k:
        min_dist_half = cur_sum-half_k
        max_min = cur_sum

print(max_min)