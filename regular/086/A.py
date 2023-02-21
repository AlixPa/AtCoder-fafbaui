import sys
def IIS(): return map(int, input().split())
def SIS(): return input().split()
def II(): return int(input())
def SI(): return input()
def FIS(): return map(float, input().split())
def FI(): return float(input())
sys.setrecursionlimit(10**8)

_, k = IIS()
ls_ai = list(IIS())

dt_ai = dict()
for ai in ls_ai:
  if ai in dt_ai:
    dt_ai[ai] += 1
  else:
    dt_ai[ai] = 1

ls_nb = list()
for ai in dt_ai:
  ls_nb.append(dt_ai[ai])

ls_nb.sort()

nb_changed = 0
for nb in ls_nb[:len(ls_nb)-k]:
  nb_changed += nb

print(nb_changed)