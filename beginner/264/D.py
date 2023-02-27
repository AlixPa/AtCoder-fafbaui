import sys
def IIS(): return map(int, input().split())
def SIS(): return input().split()
def II(): return int(input())
def SI(): return input()
def FIS(): return map(float, input().split())
def FI(): return float(input())
sys.setrecursionlimit(10**8)

ss = SI()
s = [l for l in ss]

nb = 0
for l in "redocta":
  pos_l = 0
  for l_s in s:
    pos_l += 1
    if l_s == l:
      break
  nb += len(s) - pos_l
  s.remove(l)

print(nb)