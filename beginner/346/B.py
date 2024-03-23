import sys, math
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

w, b = IIS()

wpb = w+b

if wpb >= 12:
  w -= ((wpb)//12)*7
  b -= ((wpb)//12)*5

if w == 0 and b == 0:
  print("Yes")
  sys.exit(0)

possib_nb_w = {0 : {0}, 1: {0, 1}, 2 : {1, 2}, 3 : {1, 2}, 4 : {2, 3}, 5 : {2, 3}, 6 : {3, 4}, 7 : {4, 5}, 8 : {4, 5}, 9 : {5, 6}, 10 : {5, 6}, 11 : {6, 7}}

if w in possib_nb_w[w+b]:
  print("Yes")
else:
  print("No")