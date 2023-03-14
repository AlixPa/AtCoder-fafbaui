import sys, math
from collections import deque
def IIS(): return map(int, input().split())
def SIS(): return input().split()
def II(): return int(input())
def SI(): return input()
def FIS(): return map(float, input().split())
def FI(): return float(input())
sys.setrecursionlimit(10**8)

n, m, q = IIS()
ls_abcd = list()
for _ in range(q):
  a, b, c, d = IIS()
  ls_abcd.append((a, b, c, d))

def digitSum(k):
  r = 0
  while k:
    r, k = r + k%10, k//10
  return r

def nextDigit(k):
  global m
  str_k = str(k)
  str_new_k = ""
  sum_digit = 0
  for s in str_k:
    sum_digit += int(s)
    if sum_digit >= (m-1):
      break
    str_new_k += s
  if len(str_new_k) == 0:
    return 10**(len(str(k)))
  str_new_k = str_new_k[:-1] + str(int(str_new_k[-1])+1)
  len_new = len(str_new_k)
  for _ in range(len(str_k)-len_new):
    str_new_k += "0"
  return int(str_new_k)

ls_jumps = list()
i = 0
while i < 10**(n-1):
  if digitSum(i) > (m-1):
    i = nextDigit(i)
    continue
  str_i = str(i).zfill(n-1)
  ls_jumps.append(str_i)
  i += 1

max_sum = 0
for jumps in ls_jumps:
  sum_loc = 0
  for (a, b, c, d) in ls_abcd:
    dist = 0
    for i in range(a-1, b-1):
      dist += int(jumps[i])
    if dist == c:
      sum_loc += d
  if sum_loc > max_sum:
    max_sum = sum_loc

print(max_sum)