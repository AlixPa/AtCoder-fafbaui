import sys, math
def IIS(): return map(int, input().split())
def SIS(): return input().split()
def II(): return int(input())
def SI(): return input()
def FIS(): return map(float, input().split())
def FI(): return float(input())
sys.setrecursionlimit(10**8)

n = II()
nb_progressions = 1

for i in range(2, math.ceil(math.sqrt(2*n)) + 1):
  if (n - (i*(i-1))/2)%i == 0:
    nb_progressions += 1

nb_progressions *= 2

sum_from_0 = 0
i = 1
while sum_from_0 < n:
  sum_from_0 += i
  i += 1
if sum_from_0 == n:
  nb_progressions -= 2

print(nb_progressions)