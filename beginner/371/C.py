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

G = [set() for _ in range(n)]
H = [set() for _ in range(n)]

mg = II()
for _ in range(mg):
    u, v = IIS()
    G[u-1].add(v-1)
    G[v-1].add(u-1)
mh = II()
for _ in range(mh):
    u, v = IIS()
    H[u-1].add(v-1)
    H[v-1].add(u-1)

A = list()
for _ in range(n-1):
    ls = LIIS()
    A.append(ls)

final_cost = math.inf
for ls_perm in list(itertools.permutations([i for i in range(n)])):
    cost = 0
    for i in range(n):
        for j in range(i+1, n):
            if (i in G[j] and ls_perm[i] not in H[ls_perm[j]]) or (not i in G[j] and ls_perm[i] in H[ls_perm[j]]):
                n_i = min(ls_perm[i], ls_perm[j])
                n_j = max(ls_perm[i], ls_perm[j])
                cost += A[n_i][n_j-n_i-1]
    final_cost = min(final_cost, cost)

print(final_cost)