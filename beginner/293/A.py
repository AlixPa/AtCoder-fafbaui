import sys, math
from collections import deque
def IIS(): return map(int, input().split())
def SIS(): return input().split()
def II(): return int(input())
def SI(): return input()
def FIS(): return map(float, input().split())
def FI(): return float(input())
sys.setrecursionlimit(10**8)

s = SI()
t = ""
for i in range(len(s)//2):
  t += s[(2*i)+1]
  t += s[(2*i)]
if len(s)%2 != 0:
  t += s[-1]
print(t)