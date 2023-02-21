import sys, math
def IIS(): return map(int, input().split())
def SIS(): return input().split()
def II(): return int(input())
def SI(): return input()
def FIS(): return map(float, input().split())
def FI(): return float(input())
sys.setrecursionlimit(10**8)

t = II()
def lcm(a, b):
  return abs(a*b) // math.gcd(a, b)

for _ in range(t):
  n, d, k = IIS()

  d = d%n
  relative = ((k-1)*d)%n
  if d == 0:
    print(relative + (k-1))
    continue
  collision_on_k = lcm(d, n)//d
  if collision_on_k == 0:
    nb_collision = (k-1)
  else:
    nb_collision = (k - 1)//collision_on_k
  print(relative + nb_collision)