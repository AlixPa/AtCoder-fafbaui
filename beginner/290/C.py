import sys
def IIS(): return map(int, input().split())
def SIS(): return input().split()
def II(): return int(input())
def SI(): return input()
def FIS(): return map(float, input().split())
def FI(): return float(input())
sys.setrecursionlimit(10**8)


n, k = IIS()
set_a = set(IIS())
ls_a = list(set_a)
ls_a.sort()

if ls_a[0] != 0:
  print(0)
  sys.exit(0)

max_up = 0
prev = ls_a[0] - 1

for (i, ai) in zip(range(k), ls_a):
  if ai != (prev + 1):
    break
  max_up = ai + 1
  prev = ai

print(max_up)