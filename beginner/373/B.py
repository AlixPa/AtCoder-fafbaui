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

s = SI()

nb_jumps = 0
dt_pos = dict()
for i in range(26):
    dt_pos[s[i]] = i
pos_cur = dt_pos["A"]
for i in range(25):
    nb_jumps += max(dt_pos[chr(ord("A")+i)] - dt_pos[chr(ord("A")+i+1)], dt_pos[chr(ord("A")+i+1)] - dt_pos[chr(ord("A")+i)])
    pos_cur = dt_pos[chr(ord("A")+i+1)]
print(nb_jumps)