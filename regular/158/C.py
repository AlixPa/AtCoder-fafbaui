import sys, math
from collections import deque
def IIS(): return map(int, input().split())
def SIS(): return input().split()
def II(): return int(input())
def SI(): return input()
def FIS(): return map(float, input().split())
def FI(): return float(input())
sys.setrecursionlimit(10**8)

n = II()
ls_a = list(IIS())

def digitSum(k):
  r = 0
  while k:
    r, k = r + k%10, k//10
  return r

nb_tot = 2*n*sum(map(digitSum, ls_a))

nb_collisions = 0
for b in range(1,16):
  b_pow = pow(10, b)
  ls_cur_a = [a%b_pow for a in ls_a]
  ls_cur_a.sort()
  j = 0
  for a in ls_cur_a[::-1]:
    dif_max = b_pow - a
    for i in range(j, n):
      if ls_cur_a[i] >= dif_max:
        nb_collisions += n-i
        j = i
        break
    if i == n-1 and j != i:
      break
print(nb_tot - 9*nb_collisions)
    