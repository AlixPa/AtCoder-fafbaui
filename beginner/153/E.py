import sys, math
from collections import deque
def IIS(): return map(int, input().split())
def SIS(): return input().split()
def II(): return int(input())
def SI(): return input()
def FIS(): return map(float, input().split())
def FI(): return float(input())
sys.setrecursionlimit(10**8)

h, n = IIS()
ls_spells = list()
for _ in range(n):
  a, b = IIS()
  ls_spells.append((a,b))
ls_spells.sort()
health_max = max(ls_spells[-1][0], h) + ls_spells[-1][0]
health = [False for _ in range(health_max + 1)]
health[0] = True
costs = [math.inf for _ in range(health_max + 1)]
costs[0] = 0
for i in range(health_max + 1):
  if health[i]:
    for (a, b) in ls_spells:
      next_health = i + a
      if next_health > health_max:
        break
      health[next_health] = True
      new_cost = costs[i] + b
      if new_cost < costs[next_health]:
        costs[next_health] = new_cost

min_cost = costs[h]
for i in range(1+ls_spells[-1][0]):
  if health[h+i]:
    if costs[h+i] < min_cost:
      min_cost = costs[h+i]

print(min_cost)