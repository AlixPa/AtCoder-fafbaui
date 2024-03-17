import sys, math
from collections import deque, defaultdict
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

s = SI()  

left = 0
right = len(s) - 1
nb_add = 0
while left < right:
  if s[left] == s[right]:
    left += 1
    right -= 1
  elif s[left] == "x":
    left += 1
    nb_add += 1
  elif s[right] == "x":
    right -= 1
    nb_add += 1
  else:
    print(-1)
    sys.exit(0)
print(nb_add)