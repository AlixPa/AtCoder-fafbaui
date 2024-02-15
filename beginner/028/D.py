import sys, math
from collections import deque, defaultdict
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

n, k = IIS()

print(6*( (1/n)*((n-k)/n)*((k-1)/n) ) + 1/pow(n, 3) + 3*( (1/pow(n, 2))*((n-1)/n) ))