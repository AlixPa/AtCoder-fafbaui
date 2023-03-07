import sys, math
def IIS(): return map(int, input().split())
def SIS(): return input().split()
def II(): return int(input())
def SI(): return input()
def FIS(): return map(float, input().split())
def FI(): return float(input())
sys.setrecursionlimit(10**8)

a, b, x = IIS()

volume_tot = b*pow(a,2)
if volume_tot == x:
  print(0)
  sys.exit(0)
beta = 0

if x > volume_tot/2:
  beta = math.atan(pow(a,3)/(2*(volume_tot-x)))
else:
  beta = math.atan(2*x/(a*pow(b,2)))
beta *= (180/math.pi)

print(90 - beta)