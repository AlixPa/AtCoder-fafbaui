import sys
def IIS(): return map(int, input().split())
def SIS(): return input().split()
def II(): return int(input())
def SI(): return input()
def FIS(): return map(float, input().split())
def FI(): return float(input())
sys.setrecursionlimit(10**8)

n, m = IIS()
s = list()
t = set()

for i in range(n):
  s.append(SI())
for j in range(m):
  t.add(SI())

c = 0
for st in s:
  if st[3:] in t:
    c += 1

print(c)