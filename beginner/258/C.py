import sys
def IIS(): return map(int, input().split())
def SIS(): return input().split()
def II(): return int(input())
def SI(): return input()
def FIS(): return map(float, input().split())
def FI(): return float(input())
sys.setrecursionlimit(10**8)

n, q = IIS()
s = SI()

shifted = 0

for _ in range(q):
  t, x = IIS()
  if t == 1:
    shifted -= x
    shifted %= n
  else:
    print(s[(shifted + x - 1)%n])