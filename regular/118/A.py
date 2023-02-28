import sys, math
def IIS(): return map(int, input().split())
def SIS(): return input().split()
def II(): return int(input())
def SI(): return input()
def FIS(): return map(float, input().split())
def FI(): return float(input())
sys.setrecursionlimit(10**8)

t, n = IIS()
num_shift = (float(n)/float(t))*100

if math.isclose(num_shift, math.floor(num_shift)) or math.isclose(num_shift, math.ceil(num_shift)):
  num_shift -= 1

if math.isclose(num_shift, math.ceil(num_shift)):
  print(math.ceil(num_shift + n))
else:
  print(math.floor(num_shift + n))