import sys
def IIS(): return map(int, input().split())
def SIS(): return input().split()
def II(): return int(input())
def SI(): return input()
def FIS(): return map(float, input().split())
def FI(): return float(input())
sys.setrecursionlimit(10**8)

S = SI()
T = SI()
s = len(S)
t = len(T)

i_right = -t-1
i_left = t+1

for i in range(-1, -t-1, -1):
  if S[i] != T[i]:
    if S[i] != "?" and T[i] != "?":
      i_right = i
      break

for i in range(t):
  if S[i] != T[i]:
    if S[i] != "?" and T[i] != "?":
      i_left = i
      break

for i in range(t+1):
  if i <= t + i_right:
    print("No")
  elif i > i_left:
    print("No")
  else:
    print("Yes")