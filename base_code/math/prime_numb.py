import math

def get_primes(number):
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