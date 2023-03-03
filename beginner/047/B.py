import sys
def IIS(): return map(int, input().split())
def SIS(): return input().split()
def II(): return int(input())
def SI(): return input()
def FIS(): return map(float, input().split())
def FI(): return float(input())
sys.setrecursionlimit(10**8)

w, h, n = IIS()
ai_ls = list()
coordonate_dt = {"left": [0], "right": [w], "down": [0], "up": [h]}

for _ in range(n):
  x, y, a = IIS()
  if a == 1:
    coordonate_dt["left"].append(x)
  elif a == 2:
    coordonate_dt["right"].append(x)
  elif a == 3:
    coordonate_dt["down"].append(y)
  else:
    coordonate_dt["up"].append(y)

coordonate_dt["left"].sort()
coordonate_dt["right"].sort()
coordonate_dt["down"].sort()
coordonate_dt["up"].sort()

large = coordonate_dt["right"][0] - coordonate_dt["left"][-1]
long = coordonate_dt["up"][0] - coordonate_dt["down"][-1]

if large <= 0 or long <= 0:
  print(0)
else:
  print(large*long)