import sys
def IIS(): return map(int, input().split())
def SIS(): return input().split()
def II(): return int(input())
def SI(): return input()
def FIS(): return map(float, input().split())
def FI(): return float(input())
sys.setrecursionlimit(10**8)

n, m = IIS()

max_gcd = m//n

for k in range(max_gcd, 0, -1):
  if m%k == 0:
    print(k)
    sys.exit(0)