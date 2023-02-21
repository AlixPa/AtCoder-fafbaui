import sys
def IIS(): return map(int, input().split())
def SIS(): return input().split()
def II(): return int(input())
def SI(): return input()
def FIS(): return map(float, input().split())
def FI(): return float(input())
sys.setrecursionlimit(10**8)


n = II()
s = " " + SI()
l_tab = [(n-i) for i in range(n)]

for i in range(1, n):
  for k in range(1, n-i + 1):
    if s[k] == s[k+i]:
      l_tab[i] = k - 1
      break
for l in l_tab[1:]:
  print(l)