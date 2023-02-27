import sys
def IIS(): return map(int, input().split())
def SIS(): return input().split()
def II(): return int(input())
def SI(): return input()
def FIS(): return map(float, input().split())
def FI(): return float(input())
sys.setrecursionlimit(10**8)

n = II()
cards_ls = list()
MOD = 998244353

for _ in range(n):
  a, b = IIS()
  card = (a, b)
  cards_ls.append(card)

if len(cards_ls) == 0:
  print(0)
  sys.exit(0)

if len(cards_ls) == 1:
  print(2)
  sys.exit(0)

weight_a = 1
weight_b = 1
last_a, last_b = cards_ls[0]
for card in cards_ls[1:]:
  new_a, new_b = card
  new_weight_a = 0
  new_weight_b = 0
  if last_a != new_a:
    new_weight_a += weight_a
  if last_b != new_a:
    new_weight_a += weight_b
  if last_a != new_b:
    new_weight_b += weight_a
  if last_b != new_b:
    new_weight_b += weight_b
  weight_a = new_weight_a
  weight_a %= MOD
  weight_b = new_weight_b
  weight_b %= MOD
  last_a = new_a
  last_b = new_b

weight_tot = weight_a + weight_b
weight_tot %= MOD

print(weight_tot)