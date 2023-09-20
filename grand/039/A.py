import sys, math
from collections import deque
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

S = SI()
K = II()

shift_left = 0
for l in S:
  if l == S[-1]:
    shift_left += 1
  else:
    break
shift_right = 0
for l in S[::-1]:
  if l == S[0]:
    shift_right += 1
  else:
    break
if shift_left+shift_right > len(S):
  print((len(S)*K)//2)
  sys.exit(0)

save = S[shift_left]
nb_same = 1
cpt = 0
for l in S[shift_left+1 : len(S)-shift_right]:
  if l == save:
    nb_same += 1
  else:
    save = l
    cpt += nb_same//2
    nb_same = 1
cpt += nb_same//2

cpt *= K
cpt += (K-1)*((shift_left+shift_right)//2) + shift_left//2 + shift_right//2

print(cpt)