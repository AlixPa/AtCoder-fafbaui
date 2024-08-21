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

# 1 filter names with : m a r c h
# 2 calculer m*(ar+ac+ah+rc+rh+ch) + a*(rc+rh+ch) + rch
# Pas super propre mais celavi

n = II()
d = dict()
for i in range(26):
    d[chr(ord("A")+i)] = 0
for _ in range(n):
    s = SI()
    d[s[0]] += 1

print(d["M"]*(d["A"]*(d["R"]+d["C"]+d["H"]) + d["R"]*(d["C"]+d["H"]) + d["C"]*d["H"]) + d["A"]*(d["R"]*(d["C"]+d["H"]) + d["C"]*d["H"]) + d["R"]*d["C"]*d["H"])