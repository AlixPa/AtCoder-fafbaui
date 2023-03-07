import sys
def IIS(): return map(int, input().split())
def SIS(): return input().split()
def II(): return int(input())
def SI(): return input()
def FIS(): return map(float, input().split())
def FI(): return float(input())
sys.setrecursionlimit(10**8)

n, l, r = IIS()
ls_ai = list(IIS())

ls_sum_tmp = list()
sum_ai = 0
sum_l = 0
for ai in ls_ai:
  sum_ai += ai
  sum_l += l
  ls_sum_tmp.append((sum_ai, sum_l))

ls_sum_l = list()
sum_ai_partial = 0
sum_l_partial = 0
for i in range(n):
  sum_ai_partial += ls_ai[i]
  sum_ai, sum_l = ls_sum_tmp[i]
  min_sums = min(sum_ai, sum_l, sum_ai_partial + sum_l_partial)
  ls_sum_l.append(min_sums)
  if min_sums == sum_l:
    sum_l_partial = sum_l
    sum_ai_partial = 0
  
ls_sum_tmp = list()
sum_ai = 0
sum_r = 0
for ai in ls_ai[::-1]:
  sum_ai += ai
  sum_r += r
  ls_sum_tmp.append((sum_ai, sum_r))

ls_sum_r = list()
sum_ai_partial = 0
sum_r_partial = 0
for i in range(n):
  sum_ai_partial += ls_ai[-(i+1)]
  sum_ai, sum_r = ls_sum_tmp[i]
  min_sums = min(sum_ai, sum_r, sum_ai_partial + sum_r_partial)
  ls_sum_r.append(min_sums)
  if min_sums == sum_r:
    sum_r_partial = sum_r
    sum_ai_partial = 0


ls_sum_l = [0] + ls_sum_l
ls_sum_r = [0] + ls_sum_r
ls_sum_r = ls_sum_r[::-1]
#print(ls_sum_l)
#print(ls_sum_r)

ls_sum = list()
for i in range(n+1):
  ls_sum.append(ls_sum_l[i] + ls_sum_r[i])

#print(ls_sum)

print(min(ls_sum))