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

def dichotomie(v, t):
    a = 0
    b = len(t) - 1
    while a <= b:
        m = (a + b) // 2
        if t[m] == v:
            # on a trouvé v
            return (m, m)
        elif t[m] < v:
            a = m + 1
        else:
            b = m - 1
    # on a a > b
    return (b, a)

h, w, rt, ct = IIS()
n = II()
block_col = dict()
block_row = dict()
for _ in range(n):
  r, c = IIS()
  if not c in block_col:
    block_col[c] = list()
  block_col[c].append(r)
  if not r in block_row:
    block_row[r] = list()
  block_row[r].append(c)
for col in block_col:
  block_col[col].sort()
for row in block_row:
  block_row[row].sort()

q = II()
for _ in range(q):
  d, l = SIS()
  l = int(l)
  if d == "L" or d == "R":
    if rt in block_row:
      left, right = dichotomie(ct, block_row[rt])
    else:
      left, right = -1, -2
    if left == right:
      left -= 1
      right -= 1
    if d == "L":
      if left == -1:
        ct = max(1, ct - l)
      else:
        ct = max(block_row[rt][left] + 1, ct - l)
    else:
      if right == -2 or right == len(block_row[rt]):
        ct = min(w, ct + l)
      else:
        ct = min(block_row[rt][right] - 1, ct + l)
  else:
    if ct in block_col:
      left, right = dichotomie(rt, block_col[ct])
    else:
      left, right = -1, -2
    if left == right:
      left -= 1
      right -= 1
    if d == "U":
      if left == -1:
        rt = max(1, rt - l)
      else:
        rt = max(block_col[ct][left] + 1, rt - l)
    else:
      if right == -2 or right == len(block_col[ct]):
        rt = min(h, rt + l)
      else:
        rt = min(block_col[ct][right] - 1, rt + l)
  print(f"{rt} {ct}")
