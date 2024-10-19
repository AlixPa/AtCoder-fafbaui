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

s = SI()
t = SI()

for i in range(min(len(s), len(t))):
    if s[i] != t[i]:
        print(i+1)
        sys.exit(0)
if len(s) != len(t):
    print(min(len(s), len(t))+1)
    sys.exit(0)
for i in range(len(s)):
    if s[i] != t[i]:
        print(i+1)
        sys.exit(0)
print(0)