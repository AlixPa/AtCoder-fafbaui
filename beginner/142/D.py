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

def primeFactors(number):
  '''
  Returns the list of prime factors of a number
  12 => [2, 2, 3]
  '''
  primes = list()
  while number % 2 == 0:
    primes.append(2)
    number = number / 2
  for i in range(3,int(math.sqrt(number))+1,2):
    while number % i== 0:
      primes.append(i)
      number = number // i
  if number > 2:
    primes.append(number)
  return primes

A, B = IIS()
st_prime_A = set(primeFactors(A))
st_prime_B = set(primeFactors(B))
st_inter = st_prime_A.intersection(st_prime_B)

print(len(st_inter) + 1)