import sys
def IIS(): return map(int, input().split())
def SIS(): return input().split()
def II(): return int(input())
def SI(): return input()
def FIS(): return map(float, input().split())
def FI(): return float(input())
sys.setrecursionlimit(10**8)

n = II()
c = 0
for i in range(n):
  if SI() == "For":
    c += 1

if c > n//2:
  print("Yes")
else:
  print("No")