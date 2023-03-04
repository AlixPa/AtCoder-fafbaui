import sys
def IIS(): return map(int, input().split())
def SIS(): return input().split()
def II(): return int(input())
def SI(): return input()
def FIS(): return map(float, input().split())
def FI(): return float(input())
sys.setrecursionlimit(10**8)

n, q = IIS()

players = [0 for _ in range(n+1)]

for _ in range(q):
  i, x = IIS()
  if i == 3:
    if players[x] >= 2:
      print("Yes")
    else:
      print("No")
  else:
    players[x] += i