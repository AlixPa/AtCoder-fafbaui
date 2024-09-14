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

ab, ac, bc = SIS()

if (ab == "<" and bc == "<") or (bc == ">" and ab == ">"):
    print("B")
elif (ac == "<" and bc == ">") or (bc == "<" and ac == ">"):
    print("C")
else:
    print("A")