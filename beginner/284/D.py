def iis():
  return map(int, input().split())

def sis():
  return input().split()

def ii():
  return int(input())

def si():
  return input()

def fis():
  return map(float, input().split())

def fi():
  return float(input())

def decomp_p2q(n):
  r = int(n**(1/3))
  for i in range(2, r+1):
    if n%i == 0:
      if n%(i**2) == 0:
        return (i, n//(i**2))
      else:
        return (int((n//i)**(1/2)), i)

t = ii()

for i in range(t):
  n = ii()
  p,q = decomp_p2q(n)
  print("%d %d"%(p,q))