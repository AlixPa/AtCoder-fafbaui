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

m = II()
ls_a = list()

while m != 0:
    p = int(math.log(m, 3))
    k = m//pow(3, p)
    m -= k*pow(3, p)
    ls_a += k*[p]

print(len(ls_a))
print(*ls_a)