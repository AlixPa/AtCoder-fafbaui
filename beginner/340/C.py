import sys, math
from collections import deque
from heapq import heappop, heappush
def IIS(): return map(int, input().split())
def LIIS(): return list(IIS())
def SIIS(): return set(IIS())
def SIS(): return input().split()
def II(): return int(input())
def SI(): return input()
def FIS(): return map(float, input().split())
def FI(): return float(input())
sys.setrecursionlimit(10**8)

N = II()
n_tmp = N
pow2 = 0
while n_tmp > 1:
  pow2 += 1
  n_tmp = n_tmp // 2

if N != pow(2, pow2):
  pow2 += 1

print((pow2-1)*N + 2*(pow(2, pow2-1) - (pow(2, pow2) - N)))