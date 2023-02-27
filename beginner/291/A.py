import sys
def IIS(): return map(int, input().split())
def SIS(): return input().split()
def II(): return int(input())
def SI(): return input()
def FIS(): return map(float, input().split())
def FI(): return float(input())
sys.setrecursionlimit(10**8)

s = SI()
for i in range(len(s)):
  if ord(s[i]) >= ord("A") and ord(s[i]) <= ord("Z"):
    print(i+1)
    sys.exit(0)