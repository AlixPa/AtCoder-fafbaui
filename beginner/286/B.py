import sys
def IIS(): return map(int, input().split())
def SIS(): return input().split()
def II(): return int(input())
def SI(): return input()
def FIS(): return map(float, input().split())
def FI(): return float(input())
sys.setrecursionlimit(10**8)

n = II()
s = SI()

prev = ""
nyan = ""
for c in s:
  if c == "a":
    if prev == "n":
      nyan += "y"
  prev = c
  nyan += c

print(nyan)