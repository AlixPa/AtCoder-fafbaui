import sys
def IIS(): return map(int, input().split())
def SIS(): return input().split()
def II(): return int(input())
def SI(): return input()
def FIS(): return map(float, input().split())
def FI(): return float(input())
sys.setrecursionlimit(10**8)

n, k = IIS()
s = SI()

nb_qualif = 0
sp = ""

for l in s:
  if l == "x":
    sp = sp + "x"
  else:
    if nb_qualif < k:
      sp = sp + "o"
      nb_qualif += 1
    else:
      sp = sp + "x"
    
print(sp)