import sys, math
from collections import deque, defaultdict
from heapq import heappop, heappush, heapify
def IIS(): return map(int, input().split())
def LIIS(): return list(IIS())
def SIIS(): return set(IIS())
def SIS(): return input().split()
def II(): return int(input())
def SI(): return input()
def FIS(): return map(float, input().split())
def FI(): return float(input())
sys.setrecursionlimit(10**8)

def popCount(n):
  nb = 0
  while n > 0:
    if n%2 == 1:
      nb += 1
    n = n//2
  return nb

def tableBit(n):
  ls = [0 for _ in range(60)]
  i = 0
  while n > 0:
    if n%2 == 1:
      ls[i] = 1
    n = n // 2
    i += 1
  return ls

a, b, big_c = IIS()
c = popCount(big_c)

if a+b < c or (a+b-c)%2 != 0 or abs(a-b) > c or (a+b-c)//2 > 60-c:
  print(-1)
  sys.exit(0)

nb_com = (a+b-c)//2

nb_uniq_a = a - nb_com
nb_uniq_b = b - nb_com

tb_c = tableBit(big_c)

x = [0 for _ in range(60)]
y = [0 for _ in range(60)]
for i in range(60):
  if nb_uniq_a == 0:
    if nb_uniq_b == 0:
      break
    if tb_c[i] == 1:
      y[i] = 1
      nb_uniq_b -= 1
      continue
  if tb_c[i] == 1:
    x[i] = 1
    nb_uniq_a -= 1

for i in range(60):
  if nb_com == 0:
    break
  if tb_c[i] == 0:
    x[i] = 1
    y[i] = 1
    nb_com -= 1

big_x = 0
big_y = 0
for i in range(60):
  if x[i] == 1:
    big_x += pow(2, i)
  if y[i] == 1:
    big_y += pow(2, i)

print("%d %d"%(big_x, big_y))