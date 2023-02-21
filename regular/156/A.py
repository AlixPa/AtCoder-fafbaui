import sys
def IIS(): return map(int, input().split())
def SIS(): return input().split()
def II(): return int(input())
def SI(): return input()
def FIS(): return map(float, input().split())
def FI(): return float(input())
sys.setrecursionlimit(10**8)

t = II()

for _ in range(t):
  n = II()
  s = SI()

  ## get rid of boring cases
  if n < 4:
    if s in {"", "0", "00", "000"}:
      print(0)
    elif s == "101":
      print(1)
    else:
      print(-1)
    continue
  if s == "0110":
    print(3)
    continue

  ## Find number of heads
  nb_heads = 0
  for l in s:
    if l == "1":
      nb_heads += 1

  ## If impossible no good
  if nb_heads%2 > 0:
    print(-1)
    continue

  ## If full tail good
  if nb_heads == 0:
    print(0)
    continue

  ## If more than 2 tails good
  if nb_heads > 2:
    print(nb_heads//2)
    continue

  ## If nb_heads == 2, check where they at
  first_tail = -1
  second_tail = -1
  for (l, i) in zip(s, range(n)):
    if l == "1":
      if first_tail < 0:
        first_tail = i
      else:
        second_tail = i
  if second_tail - first_tail >= 2:
    print(nb_heads//2)
  else:
    print((nb_heads//2) + 1)