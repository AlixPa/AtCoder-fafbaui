import sys, math
def IIS(): return map(int, input().split())
def SIS(): return input().split()
def II(): return int(input())
def SI(): return input()
def FIS(): return map(float, input().split())
def FI(): return float(input())
sys.setrecursionlimit(10**8)

def primeFactors(n):
  primes = list()
  while n % 2 == 0:
    primes.append(2)
    n = n / 2
  for i in range(3,int(math.sqrt(n))+1,2):
    while n % i== 0:
      primes.append(i)
      n = n / i
  if n > 2:
    primes.append(n)
  return primes

def uniquesLs(ls):
  if len(ls) <= 1:
    return ls
  new_ls = list()
  last  = ls[0]
  nb_last = 1
  for k in ls[1:]:
    if k != last:
      if nb_last == 1:
        new_ls.append(last)
      nb_last = 1
      last = k
    else:
      nb_last += 1
  if ls[-1] != ls[-2]:
    new_ls.append(ls[-1])
  return new_ls

def lsOfLsNonUnique(ls):
  ls = ls.copy()
  uniques_ls = uniquesLs(ls)
  for u in uniques_ls:
    ls.remove(u)
  if len(ls) == 0:
    return [list()]
  ls_of_ls = list()
  tmp_ls = [ls[0]]
  last = ls[0]
  for k in ls[1:]:
    if k == last:
      tmp_ls.append(k)
    else:
      ls_of_ls.append(tmp_ls)
      tmp_ls = [k]
      last = k
  if len(tmp_ls) > 0:
    ls_of_ls.append(tmp_ls)
  return ls_of_ls

n = II()

if n == 2:
  print(1)
  sys.exit(0)

primes_ls = [primeFactors(i) for i in range(2, n)]
primes_ls = [list(), list()] + primes_ls
primes_uniques = [uniquesLs(primes) for primes in primes_ls]
primes_non_uniques = [lsOfLsNonUnique(primes) for primes in primes_ls]

nb_ways_xy = [pow(2, len(primes)) for primes in primes_uniques]
for i in range(len(nb_ways_xy)):
  if len(primes_non_uniques[i]) > 0:
    sum_ls = 0
    for ls in primes_non_uniques[i]:
      nb_ways_xy[i] *= (len(ls) + 1)

nb_tot = 0
for i in range(1, n):
  nb_tot += nb_ways_xy[i]*nb_ways_xy[n-i]

print(nb_tot)