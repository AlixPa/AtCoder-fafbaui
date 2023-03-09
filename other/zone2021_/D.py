import sys
from collections import deque
def IIS(): return map(int, input().split())
def SIS(): return input().split()
def II(): return int(input())
def SI(): return input()
def FIS(): return map(float, input().split())
def FI(): return float(input())
sys.setrecursionlimit(10**8)

s = SI()

t = deque(list())
rev = 0

for l in s:
  if l == "R":
    rev += 1
    rev %= 2
  else:
    if rev == 0:
      t.append(l)
    else:
      t.appendleft(l)

if len(t) == 0:
  print("")
  sys.exit(0)

if rev == 1:
  t.reverse()

res = deque(list())
for l in t:
  if len(res) == 0:
    res.append(l)
  else:
    if l == res[-1]:
      res.pop()
    else:
      res.append(l)

print("".join(res))
