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

_ = II()
lw_w = SIS()

st_words = {"and", "not", "that", "the", "you"}
for word in st_words:
  if word in lw_w:
    print("Yes")
    sys.exit(0)
print("No")