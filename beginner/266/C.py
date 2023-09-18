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

def verifConv(pts, origine):
  for i in range(4):
    pts[(origine+i+1)%4][0] -= pts[origine][0]
    pts[(origine+i+1)%4][1] -= pts[origine][1]
  comp = 0
  if pts[(origine+2)%4][0] == 0:
    for i in [1, 3]:
      if pts[(origine+i)%4][0] < 0:
        comp += 1
      else:
        comp -= 1
  else:
    coef_dir = pts[(origine+2)%4][1]/pts[(origine+2)%4][0]
    for i in [1, 3]:
      if pts[(origine+i)%4][1] < pts[(origine+i)%4][0]*coef_dir:
        comp += 1
      else:
        comp -= 1
  if comp != 0:
    print("No")
    sys.exit(0)

ls_pts = [LIIS() for _ in range(4)]

for i in range(4):
  verifConv(pts=ls_pts, origine=i)

print("Yes")