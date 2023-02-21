## THIS CODE IS AWEFUL,
## but the idea is to generate every integer from 1 to max(Ai), remembering their prime composition (self.already_prime_st in first class)
## with this, we will be able to get all the prime numbers composing all the Ai ()
## from this, we will then be able to extract every k < M such that k has one of the AI prime (because then, gcd(k, Ai) == this prime > 1)
## We will then (more or less):
### 1: Generate all prime numbers from 1 to my_max = MAX(max(Ai), k) (for simplicity we will use both time the same list)
### 2: Generate all integers from 1 to my_max, and if one of this integer is an Ai, then we will remember its prime composition in k_bool
### 3: Exclude all these prime numbers composing the Ai of or initial list
### 4: Generate all integers possible in the range [1, M] with this reduced prime list

## Note that most of the variable have stupid names and not always corresponding... sorry

import sys
def IIS(): return map(int, input().split())
def SIS(): return input().split()
def II(): return int(input())
def SI(): return input()
def FIS(): return map(float, input().split())
def FI(): return float(input())
sys.setrecursionlimit(10**8)

def SieveOfEratosthenes(num):
  prime = [True for i in range(num+1)]
  p = 2
  while (p * p <= num):
    # If prime[p] is not
    # changed, then it is a prime
    if (prime[p] == True):
      # Updating all multiples of p
      for i in range(p * p, num+1, p):
        prime[i] = False
    p += 1  
  prime_ls = list()
  for p in range(2, num+1):
    if prime[p]:
      prime_ls.append(p)
  return prime_ls

n, m = IIS()
ai_st = set(IIS())

#pow_10_5 = pow(10,5)
#pow_10_5 = 4000
my_max = max(ai_st)
my_max = max(my_max, m)

is_in_st = [False]*(my_max + 1)
for ai in ai_st:
  is_in_st[ai] = True

prime_to_m = SieveOfEratosthenes(my_max)

prime_to_m = [1] + prime_to_m
nb_prime = len(prime_to_m)

k_bool = [True]*(nb_prime)

#nb_gen = 0
class generateAllNumbers:
  def __init__(self, mult_cur, index_cur, already_prime_st):
    self.mult_cur = mult_cur
    self.index_cur = index_cur
    self.already_prime_st = already_prime_st

  def next_step(self):
    global my_max
    global is_in_st
    global k_bool
    global nb_prime
    global prime_to_m
    #global nb_gen
    #nb_gen += 1
    
    self.already_prime_st.add(self.index_cur)
    if is_in_st[self.mult_cur]:
      for i in self.already_prime_st:
        k_bool[i] = False

    for i in range(self.index_cur, nb_prime):
      mult_tmp = self.mult_cur * prime_to_m[i]
      if mult_tmp > my_max:
        return
      new_generateAll = generateAllNumbers(mult_tmp, i, self.already_prime_st.copy())
      new_generateAll.next_step()

for i in range(1, nb_prime):
  first_generateAll = generateAllNumbers(prime_to_m[i], i, set())
  first_generateAll.next_step()
#print(nb_gen)
k_prime_ls = list()
for i in range(len(prime_to_m)):
  if k_bool[i]:
    k_prime_ls.append(prime_to_m[i])

k_ls = list()
class generateAllNumbers2:
  def __init__(self, mult_cur, index_cur):
    self.mult_cur = mult_cur
    self.index_cur = index_cur

  def next_step(self):
    global k_prime_ls

    k_ls.append(self.mult_cur)

    for i in range(self.index_cur, len(k_prime_ls)):
      mult_tmp = self.mult_cur * k_prime_ls[i]
      if mult_tmp > m:
        return
      new_generateAll = generateAllNumbers2(mult_tmp, i)
      new_generateAll.next_step()

first_generateAll2 = generateAllNumbers2(1, 1)
first_generateAll2.next_step()

k_ls.sort()
print(len(k_ls))
for p in k_ls:
  print(p)