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

# Idea : Try a lot of modulo ? Who knows
# Note also that as writing all monster health as H = gcd*mi, we can just output gcd lol

n = II()
ls_a = LIIS()

ls_a.sort()
nb_mod = 1

while (ls_a[0] != 1 and nb_mod > 0):
    nb_mod = 0
    for i in range(n-1):
        nb = ls_a[i+1]%ls_a[0]
        if nb != 0:
            nb_mod += 1
            ls_a[i+1] = nb
    ls_a.sort()

print(ls_a[0])