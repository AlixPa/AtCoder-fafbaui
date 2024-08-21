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

# The global speed is the speed of the slowest
# Plus add a full travel time

n = II()
a = II()
b = II()
c = II()
d = II()
e = II()

slowest = min(a, b, c, d, e)
shift = 4
if n%slowest != 0:
    shift += 1
print(shift + n//slowest)