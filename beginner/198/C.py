import sys, math
def IIS(): return map(int, input().split())
def SIS(): return input().split()
def II(): return int(input())
def SI(): return input()
def FIS(): return map(float, input().split())
def FI(): return float(input())
sys.setrecursionlimit(10**8)

r, x, y = IIS()

dist_0 = math.sqrt(x*x + y*y)
nb_r = dist_0//r

if not math.isclose(dist_0, nb_r*r):
  nb_r += 1
if dist_0 < r:
  nb_r += 1

print(int(nb_r))