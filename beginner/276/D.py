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

# Idea : 
# 1 : Check the gcd
# 2 : Divide everything by gcd
# 3 : Divide everything by 2 and 3, counting the nb of time division is operated
# 4 : If everithing is 1 then possible else not

# I did differently but anyway,  same idea

n = II()
ls_a = LIIS()

gcd = math.gcd(* ls_a)
nb_divide = 0
for i in range(n):
    ls_a[i] /= gcd
    while ls_a[i]%2 == 0:
        nb_divide += 1
        ls_a[i] /= 2
    while ls_a[i]%3 == 0:
        nb_divide += 1
        ls_a[i] /= 3

ls_a.sort()
if ls_a[0] == ls_a[-1]:
    print(nb_divide)
else:
    print(-1)