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
ls_a = LIIS()

dt_a = dict()
ls_next = [-1 for _ in range(n-1)]

for i in range(n):
    if ls_a[i] not in dt_a:
        dt_a[ls_a[i]] = i
    else:
        ls_next[dt_a[ls_a[i]]] = i
        dt_a[ls_a[i]] = i

ls_sum = [0 for _ in range(n)]
st_dif = set()
cur_dif = 0
for a in ls_a:
    if a not in st_dif:
        st_dif.add(a)
        cur_dif += 1
    ls_sum[0] += cur_dif

for i in range(1, n):
    ls_sum[i] = ls_sum[i-1]
    if ls_next[i-1] != -1:
        ls_sum[i] -= (ls_next[i-1]-i+1)
    else:
        ls_sum[i] -= (n-i+1)

print(sum(ls_sum))