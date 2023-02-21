import sys
def IIS(): return map(int, input().split())
def SIS(): return input().split()
def II(): return int(input())
def SI(): return input()
def FIS(): return map(float, input().split())
def FI(): return float(input())
sys.setrecursionlimit(10**8)

n, a, b = IIS()
ss = SI()
s = list()
for c in ss:
  s.append(ord(c))

tab_palB = list()
cost_i = 0
k = 0
for i in range(n):
  cost_i = 0
  for j in range(n//2):
    k = i+j
    l = i - j - 1
    if k >= n:
      k -= n
    if l >= n:
      l -= n
    if s[k] != s[l]:
      cost_i += b
  tab_palB.append(cost_i)

for i in range(n):
  tab_palB[i] += i*a

print(min(tab_palB))