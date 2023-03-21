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

def my_range(start,end,base,step=1):
  def Convert(n,base):
    string = "0123456789ABCDEF"
    if n < base:
      return string[n]
    else:
      return Convert(n//base,base) + string[n%base]
  return (Convert(i,base) for i in range(start,end,step))

n = II()
ls_fijk = [LIIS() for _ in range(n)]
ls_pij = [LIIS() for _ in range(n)]

nb_max = -math.inf
for schedule in my_range(start=1, end=pow(2, 10)+1, base=2):
  schedule = schedule.zfill(10)
  tmp_max = 0
  nb_com = 0
  for j in range(10):
    if ls_fijk[0][j] == 1 and schedule[j] == "1":
      nb_com += 1
  tmp_max = ls_pij[0][nb_com]
  for i in range(1, n):
    nb_com = 0
    for j in range(10):
      if ls_fijk[i][j] == 1 and schedule[j] == "1":
        nb_com += 1
    tmp_max += ls_pij[i][nb_com]
  if tmp_max > nb_max:
    nb_max = tmp_max

print(nb_max)
