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

for i in range(8):
  s = SI()
  if "*" in s:
    break
for _ in range(i+1, 8):
  _ = SI()
for j in range(8):
  if s[j] == "*":
    break

print("{}{}".format(chr(ord("a")+j), 8-i))