import sys, math
from collections import deque
def IIS(): return map(int, input().split())
def SIS(): return input().split()
def II(): return int(input())
def SI(): return input()
def FIS(): return map(float, input().split())
def FI(): return float(input())
sys.setrecursionlimit(10**8)

n, m = IIS()
edges = [list() for _ in range(2*n)]
for k in range(n):
  edges[2*k].append(2*k+1)
  edges[2*k+1].append(2*k)
for _ in range(m):
  inpt = input()
  abcd = inpt.split(sep=" ")
  a = (int(abcd[0])-1)*2
  c = (int(abcd[2])-1)*2
  if abcd[1] == "R":
    a += 1
  if abcd[3] == "R":
    c += 1
  edges[a].append(c)
  edges[c].append(a)

seen = [False for _ in range(2*n)]
def dfsSpe(cur, prev):
  seen[cur] = True
  neighboors = edges[cur]
  for neighboor in neighboors:
    if neighboor == prev:
      continue
    else:
      if not seen[neighboor]:
        dfsSpe(cur=neighboor, prev=cur)

nb_non_cycles = 0
for i in range(2*n):
  if not seen[i]:
    if len(edges[i]) == 1:
      dfsSpe(cur=i, prev=-1)
      nb_non_cycles += 1
nb_cycles = 0
for i in range(2*n):
  if not seen[i]:
    dfsSpe(cur=i, prev=-1)
    nb_cycles += 1

print(f"{nb_cycles} {nb_non_cycles}")
