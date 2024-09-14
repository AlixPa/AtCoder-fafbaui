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

def checkConsec(ls_grid, i, j, ls_nb, i_ls):
    if ls_grid[i][j] == "#":
        ls_nb[i_ls][0][-1] += 1
    else:
        if ls_nb[i_ls][1] >= 2:
            ls_nb[i_ls][0] = ls_nb[i_ls][0][1:] + [0]
        else:
            ls_nb[i_ls][0] = ls_nb[i_ls][0] + [0]
            ls_nb[i_ls][1] += 1
    if sum(ls_nb[i_ls][0])+ls_nb[i_ls][1] >= 6:
        print("Yes")
        sys.exit(0)
    return

ls_grid = list()

n = II()
for _ in range(n):
    S = SI()
    ls_grid.append(S)



for i in range(n):
    ls_nb = [[[0], 0] for _ in range(6)]
    for j in range(n):
        checkConsec(ls_grid, i, j, ls_nb, 0)
        checkConsec(ls_grid, j, i, ls_nb, 1)
        if i-j >= 0:
            checkConsec(ls_grid, i-j, j, ls_nb, 2)
        if i+j <= n-1:
            checkConsec(ls_grid, n-1-j, i+j, ls_nb, 3)
            checkConsec(ls_grid, j, i+j, ls_nb, 4)
            checkConsec(ls_grid, i+j, j, ls_nb, 5)

print("No")