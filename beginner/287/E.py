import sys
def IIS(): return map(int, input().split())
def SIS(): return input().split()
def II(): return int(input())
def SI(): return input()
def FIS(): return map(float, input().split())
def FI(): return float(input())
sys.setrecursionlimit(10**8)

class mot_spe:
  def __init__(self, s, i):
    self.mot = s
    self.i = i

n = II()

ls_ms = list()
ls_lcp = [0 for _ in range(n)]
for i in range(n):
  ls_ms.append(mot_spe(SI(), i))

class grp:
  def __init__(self, ms_ls, last_let, last_i):
    self.ms_ls = ms_ls
    self.last_let = last_let
    self.last_i = last_i
  def next_step(self):
    dt_ms = dict()
    i = self.last_i + 1
    for ms in self.ms_ls:
      if len(ms.mot) == i:
        ls_lcp[ms.i] = i
      else:
        if ms.mot[i] in dt_ms:
          dt_ms[ms.mot[i]].append(ms)
        else:
          dt_ms[ms.mot[i]] = [ms]
    for key in dt_ms:
      ls_ms = dt_ms[key]
      if len(ls_ms) == 1:
        ms = ls_ms[0]
        ls_lcp[ms.i] = i
        continue
      new_grp = grp(ls_ms, key, i)
      new_grp.next_step()

new_grp = grp(ls_ms, "", -1)
new_grp.next_step()

for lcp in ls_lcp:
  print(lcp)