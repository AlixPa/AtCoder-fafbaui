import sys, math
from collections import deque
def IIS(): return map(int, input().split())
def SIS(): return input().split()
def II(): return int(input())
def SI(): return input()
def FIS(): return map(float, input().split())
def FI(): return float(input())
sys.setrecursionlimit(10**8)

t = II()
for _ in range(t):
  ls_x = list(IIS())
  ls_x.sort()
  if ls_x[0]%2 == 0:
    if ls_x[1]%2 != 0 or ls_x[2]%2 != 0:
      print(-1)
      continue
  else:
    if ls_x[1]%2 == 0 or ls_x[2]%2 == 0:
      print(-1)
      continue
  if (2*ls_x[2]-ls_x[1]-ls_x[0])%6 != 0:
    print(-1)
    continue
  nb_needed_tot = 0
  nb_needed2 = (ls_x[2]-ls_x[1])//2
  nb_needed4 = (ls_x[2]-ls_x[0])//4
  if nb_needed2 > nb_needed4:
    nb_needed2 = (ls_x[1]-ls_x[0])//2
    nb_needed_tot += nb_needed2
    ls_x[0] += 4*nb_needed2
    ls_x[1] += 2*nb_needed2
    nb_needed6 = (ls_x[2]-ls_x[1])//6
    nb_needed_tot += 2*nb_needed6
    ls_x[0] += 6*nb_needed6
    ls_x[1] += 6*nb_needed6
  else:
    nb_needed_tot += nb_needed2
    ls_x[0] += 4*nb_needed2
    ls_x[1] += 2*nb_needed2
    dif = ls_x[2] - ls_x[0]
    nb_needed6 = dif//6
    nb_needed_tot += 2*nb_needed6
  print(nb_needed_tot)