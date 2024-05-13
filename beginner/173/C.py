import sys, math, copy, itertools
from collections import deque, defaultdict
from heapq import heappop, heappush, heapify
def IIS(): return map(int, input().split())
def LIIS(): return list(IIS())
def SIIS(): return set(IIS())
def SIS(): return input().split()
def II(): return int(input())
def SI(): return input()
def FIS(): return map(float, input().split())
def FI(): return float(input())
sys.setrecursionlimit(10**8)

def powerset(iterable):
  "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
  s = list(iterable)  # allows duplicate elements
  return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s)+1))

h, w, k = IIS()
mat = list()

for _ in range(h):
  ls = SI()
  mat.append(ls)

nb = 0
for ls_h, ls_w in itertools.product(powerset([i for i in range(h)]), powerset([i for i in range(w)])):
  nb_black = 0
  for i_h in range(h):
    if i_h in ls_h:
      continue
    for i_w in range(w):
      if i_w in ls_w:
        continue
      if mat[i_h][i_w] == "#":
        nb_black += 1
  if nb_black == k:
    nb += 1

print(nb)
