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
called = [False for _ in range(n+1)]
for i in range(n):
  if not called[i+1]:
    called[ls_a[i]] = True
k = 0
print_k = list()
for i in range(1, n+1):
  if not called[i]:
    k += 1
    print_k.append(str(i))
print(k)
print(" ".join(print_k))