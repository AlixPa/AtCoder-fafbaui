import sys, math
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

n = II()
s = SI()
ls_c = LIIS()

cost_left_0 = [0 if s[0] == "0" else ls_c[0]]
cost_left_1 = [0 if s[0] == "1" else ls_c[0]]
for i in range(1, n):
  if i%2 == 0:
    if s[i] == "0":
      cost_left_0.append(cost_left_0[-1])
      cost_left_1.append(cost_left_1[-1] + ls_c[i])
    else:
      cost_left_0.append(cost_left_0[-1] + ls_c[i])
      cost_left_1.append(cost_left_1[-1])
  else:
    if s[i] == "1":
      cost_left_0.append(cost_left_0[-1])
      cost_left_1.append(cost_left_1[-1] + ls_c[i])
    else:
      cost_left_0.append(cost_left_0[-1] + ls_c[i])
      cost_left_1.append(cost_left_1[-1])

cost_right_0 = [0 if int(s[-1]) != n%2 else ls_c[-1]]
cost_right_1 = [0 if int(s[-1]) == n%2 else ls_c[-1]]
for i in range(2, n+1):
  if n%2 == i%2:
    if s[-i] == "0":
      cost_right_0.append(cost_right_0[-1])
      cost_right_1.append(cost_right_1[-1] + ls_c[-i])
    else:
      cost_right_0.append(cost_right_0[-1] + ls_c[-i])
      cost_right_1.append(cost_right_1[-1])
  else:
    if s[-i] == "1":
      cost_right_0.append(cost_right_0[-1])
      cost_right_1.append(cost_right_1[-1] + ls_c[-i])
    else:
      cost_right_0.append(cost_right_0[-1] + ls_c[-i])
      cost_right_1.append(cost_right_1[-1])

min_cost = cost_left_0[0] + cost_right_1[-2]
for i in range(n-1):
  if cost_left_0[i] + cost_right_1[-(i+2)] < min_cost:
    min_cost = cost_left_0[i] + cost_right_1[-(i+2)]
  if cost_left_1[i] + cost_right_0[-(i+2)] < min_cost:
    min_cost = cost_left_1[i] + cost_right_0[-(i+2)]
  
print(min_cost)