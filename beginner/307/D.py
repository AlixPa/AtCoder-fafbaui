import sys, math
from collections import deque, defaultdict
from heapq import heappop, heappush
def IIS(): return map(int, input().split())
def LIIS(): return list(IIS())
def SIIS(): return set(IIS())
def SIS(): return input().split()
def II(): return int(input())
def SI(): return input()
def FIS(): return map(float, input().split())
def FI(): return float(input())
sys.setrecursionlimit(10**8)

n = II()
s = SI()

q = deque()
sup_int = list()

for i in range(n):
  if s[i] == "(":
    q.append(i)
  if s[i] == ")":
    if len(q) != 0:
      l = q.pop()
      sup_int.append([l, i])

if len(sup_int) == 0:
  print(s)
  sys.exit(0)

sup_int.sort()
new_sup_int = [sup_int[0]]
for e in sup_int[1:]:
  l = e[0]
  r = e[1]
  if l > new_sup_int[-1][1]:
    new_sup_int.append([l, r])

to_print = ""
left = 0
for e in new_sup_int:
  l = e[0]
  r = e[1]
  to_print = to_print + s[left:l]
  left = r + 1
to_print = to_print + s[left:]
print(to_print)