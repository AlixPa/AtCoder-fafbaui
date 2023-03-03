import sys
def IIS(): return map(int, input().split())
def SIS(): return input().split()
def II(): return int(input())
def SI(): return input()
def FIS(): return map(float, input().split())
def FI(): return float(input())
sys.setrecursionlimit(10**8)

x, k, d = IIS()
x = abs(x)

nb_to_min = round(x/d)

if k > nb_to_min:
  k -= nb_to_min
  x -= nb_to_min*d
  x = abs(x)
  k %= 2

print(abs(x - k*d))