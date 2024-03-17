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

t = II()
for _ in range(t):
  a1, a2, a3, a4, a5 = IIS()
  _, _, _, p4, p5 = IIS()
  cw = a1 + 2*a2 + 3*a3 + 4*a4 + 5*a5
  cs = a1 + a2 + a3 + a4 + a5
  if cw/cs >= 3:
    print(0)
    continue
  need_sup = 3*cs - cw
  if p5 <= p4:
    print(p5*math.ceil(need_sup/2))
  elif p5 >= 2*p4:
    print(p4*need_sup)
  else:
    if need_sup%2 == 0:
      print(p5*(need_sup//2))
    else:
      print(p5*(need_sup//2)+p4)