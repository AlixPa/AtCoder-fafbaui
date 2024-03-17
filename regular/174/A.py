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

def maxSubArraySum(a,size):
  max_so_far =a[0]
  curr_max = a[0]
  index = 0
  for i in range(1,size):
    curr_max = max(a[i], curr_max + a[i])
    if curr_max > max_so_far:
      index = i
      max_so_far = curr_max 
  return index, max_so_far

def minSubArraySum(a,size):
  min_so_far =a[0]
  curr_min = a[0]
  index = 0
  for i in range(1,size):
    curr_min = min(a[i], curr_min + a[i])
    if curr_min < min_so_far:
      index = i
      min_so_far = curr_min 
  return index, min_so_far

n, c = IIS()
ls_a = LIIS()

if c > 0:
  index_right, sum_sub = maxSubArraySum(ls_a, n)
  if sum_sub <= 0:
    print(sum(ls_a))
    sys.exit(0)
else:
  index_right, sum_sub = minSubArraySum(ls_a, n)
  if sum_sub >= 0:
    print(sum(ls_a))
    sys.exit(0)

index_left = index_right
sum_tmp = ls_a[index_right]
while sum_tmp != sum_sub:
  index_left -= 1
  sum_tmp += ls_a[index_left]

sum_tot = 0
for i in range(n):
  if i >= index_left and i <= index_right:
    sum_tot += c*ls_a[i]
  else:
    sum_tot += ls_a[i]

print(sum_tot)