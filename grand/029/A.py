import sys
def IIS(): return map(int, input().split())
def SIS(): return input().split()
def II(): return int(input())
def SI(): return input()
def FIS(): return map(float, input().split())
def FI(): return float(input())
sys.setrecursionlimit(10**8)

s = SI()

s = s[::-1]

nb_ope = 0
nb_black = 0
for (i, l) in zip (range(len(s)), s):
  if l == "B":
    nb_ope += (i - nb_black)
    nb_black += 1

print(nb_ope)