import sys, math
from collections import deque
def IIS(): return map(int, input().split())
def LIIS(): return list(IIS())
def SIIS(): return set(IIS())
def SIS(): return input().split()
def II(): return int(input())
def SI(): return input()
def FIS(): return map(float, input().split())
def FI(): return float(input())
sys.setrecursionlimit(10**8)

n, k = IIS()
s = SI()

ls_nb01 = list()
prev = 1
nb = 0
for c in s:
  if int(c) == prev:
    nb += 1
  else:
    prev += 1
    prev %= 2
    ls_nb01.append(nb)
    nb = 1
ls_nb01.append(nb)

max_consec = 0
current_consec = 0
consec = 0
for i in range(len(ls_nb01)):
  nb01 = ls_nb01[i]
  current_consec += nb01
  if i%2 != 0 and i//2 >= k:
    current_consec -= (ls_nb01[i-2*k] + ls_nb01[i-(2*k + 1)])
  if current_consec > max_consec:
    max_consec = current_consec

print(max_consec)