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

A, B, C, D = IIS()


nb_Cmult = B//C - (A-1)//C
nb_Dmult = B//D - (A-1)//D

gcd = math.gcd(C, D)
com_mult = (C//gcd)*D
nb_coll = (B//com_mult) - ((A-1)//com_mult)

print((B-A+1) - (nb_Cmult + nb_Dmult - nb_coll))