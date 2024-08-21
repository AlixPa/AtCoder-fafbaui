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

# Coming from right to left, considering aaaaaabbbb as k = 1
# If we shift one b from right to the left such that we have baaaaaabbb, then we skipped comb(b+a-1, b) combinaison
# ie all combinaisons from the word a + [aaaaabbbb] (with the [] varing combinasons)
# so each step if comb(b+a-1, b) is >= k it means that we have our k in the [aaaaabbbb] rest
# else, we have to consider the word b + [aaaaaabbb] and substract this comb to k

a, b, k = IIS()

res = ""
while a+b > 0:
    cb = math.comb(b+a-1, b)
    if cb >= k:
        res += "a"
        a -= 1
    else:
        res += "b"
        b -= 1
        k -= cb

print(res)