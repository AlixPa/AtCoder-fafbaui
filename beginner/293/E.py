import sys, math
from collections import deque
def IIS(): return map(int, input().split())
def SIS(): return input().split()
def II(): return int(input())
def SI(): return input()
def FIS(): return map(float, input().split())
def FI(): return float(input())
sys.setrecursionlimit(10**8)

a, x, MOD = IIS()

if a == 1:
  print(x%MOD)
else:
  print(int( ((pow(a,x,MOD*(a-1))-1)%(MOD*(a-1))) / (a-1) ))