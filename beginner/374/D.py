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

n, s, t = IIS()
ls_abcd = list()

for _ in range(n):
    a, b, c, d = IIS()
    ls_abcd.append((a, b, c, d))

mat_dep = [[0]*2*n for _ in range(2*n)]
for i in range(n):
    for j in range(n):
        xil, yil, xir, yir = ls_abcd[i]
        xjl, yjl, xjr, yjr = ls_abcd[j]
        mat_dep[2*i][2*j] = pow(pow(xil-xjl, 2) + pow(yil-yjl, 2), 0.5)
        mat_dep[2*i][2*j + 1] = pow(pow(xil-xjr, 2) + pow(yil-yjr, 2), 0.5)
        mat_dep[2*i + 1][2*j] = pow(pow(xir-xjl, 2) + pow(yir-yjl, 2), 0.5)
        mat_dep[2*i + 1][2*j + 1] = pow(pow(xir-xjr, 2) + pow(yir-yjr, 2), 0.5)

ls_print = [pow(pow(xl-xr, 2) + pow(yl-yr, 2), 0.5) for (xl, yl, xr, yr) in ls_abcd]
print_cost = sum(ls_print)

min_cost = math.inf
for ls in list(itertools.permutations([i for i in range(n)])):
    for line_bit in range(pow(2, n)):
        cur_cost = 0
        x0l, y0l, x0r, y0r = ls_abcd[ls[0]]
        if line_bit%2 == 0:
            cur_cost += pow(pow(x0l, 2)+pow(y0l, 2), 0.5)
        else:
            cur_cost += pow(pow(x0r, 2)+pow(y0r, 2), 0.5)
        for i in range(n-1):
            cur_cost += mat_dep[2*ls[i] + (((line_bit//pow(2,i))+1)%2)][2*ls[i+1] + ((line_bit//pow(2,i+1))%2)]
        min_cost = min(min_cost, cur_cost)

print(min_cost/s + print_cost/t)