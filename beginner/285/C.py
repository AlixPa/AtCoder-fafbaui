import sys
def IIS(): return map(int, input().split())
def SIS(): return input().split()
def II(): return int(input())
def SI(): return input()
def FIS(): return map(float, input().split())
def FI(): return float(input())
sys.setrecursionlimit(10**8)


s = SI()
n = 0
i = 0
for c in s[::-1]:
  n += (ord(c) - ord("A") + 1) * pow(26, i)
  i += 1
print(n)