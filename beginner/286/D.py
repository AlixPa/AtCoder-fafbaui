import sys
def IIS(): return map(int, input().split())
def SIS(): return input().split()
def II(): return int(input())
def SI(): return input()
def FIS(): return map(float, input().split())
def FI(): return float(input())
sys.setrecursionlimit(10**8)

n, x = IIS()

atteint = [False for i in range(x + 1)]
atteint[0] = True
tmp_atteint = atteint.copy()

for i in range(n):
  a,b = IIS()
  for j in range(x + 1):
    if atteint[j]:
      try:
        for k in range(1, b+1):
          tmp_atteint[j + k*a] = True
      except:
        pass
  atteint = tmp_atteint.copy()

if atteint[x]:
  print("Yes")
else:
  print("No")
