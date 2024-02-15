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
ls_a = LIIS()

ls_a.sort()
nb_neg = 0
for e in ls_a:
  if e < 0:
    nb_neg += 1
  else:
    break

d = deque(ls_a)
if nb_neg == n:
  a = d.pop()
  d.appendleft(a)
  nb_neg -= 1
if nb_neg == 0:
  nb_neg += 1

# first to substract will become neg
tmp_sum = d.popleft()
ls_ope = list()
# then the 2 to k = n-(nb_neg+1) will become pos
for _ in range(n-nb_neg-1):
  a = d.pop()
  ls_ope.append((tmp_sum, a))
  tmp_sum -= a
# the last will become pos
a = d.pop()
ls_ope.append((a, tmp_sum))
tmp_sum = a - tmp_sum
# then the k + 1 = n-(nb_neg+1)+1 to n-1 will become neg
for _ in range(nb_neg-1):
  a = d.pop()
  ls_ope.append((tmp_sum, a))
  tmp_sum -= a

print(tmp_sum)
for x, y in ls_ope:
  print("%d %d"%(x,y))