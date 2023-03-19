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

n = II()
ls_dif = list()
for _ in range(n):
  a, b = IIS()
  ls_dif.append((a + b, a, b))
ls_dif.sort(reverse=True)
end_value = 0
for i in range(n):
  _, a, b = ls_dif[i]
  if i%2 == 0:
    end_value += a
  else:
    end_value -= b
print(end_value)