import math

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

def getPrimesToNumber(number):
  '''
  Returns the list of prime factors under a certain number
  10 => [2, 3, 5, 7]
  '''
  prime_number = []
  for i in range(2, number + 1):
    prime_number.append(i)
  i = 2
  # Here we will go from 2 to sqrt(number)
  while i <= int(math.sqrt(number)):
    # if i is in the list we will delete the multiples
    if i in prime_number:
      # Here j will give the multiples of i,
      # Here we will be starting from 2*i
      for j in range(i * 2, number + 1, i):
        if j in prime_number:
          # Here we will be deleting the multiple if found in the list
          prime_number.remove(j)
    i = i + 1
  return prime_number