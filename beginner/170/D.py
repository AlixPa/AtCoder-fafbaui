import sys
def IIS(): return map(int, input().split())
def SIS(): return input().split()
def II(): return int(input())
def SI(): return input()
def FIS(): return map(float, input().split())
def FI(): return float(input())
sys.setrecursionlimit(10**8)

n = II()
ai_ls = list(IIS())
ai_ls.sort()

if len(ai_ls) == 0:
  print(0)
  sys.exit(0)
max_ai = ai_ls[-1]

seen = [False]*(max_ai+1)

ai_st = set(ai_ls)
for ai in ai_st:
  i = 2
  iai = i*ai
  while iai <= max_ai:
    seen[iai] = True
    i += 1
    iai = i*ai

ai_unique = list()
cur_ai = ai_ls[0]
count = 1
for ai in ai_ls[1:]:
  if ai != cur_ai:
    if count == 1:
      ai_unique.append(cur_ai)
    cur_ai = ai 
    count = 1
  else:
    count += 1
if len(ai_ls) < 2:
  print(1)
  sys.exit(0)
if ai_ls[-1] != ai_ls[-2]:
  ai_unique.append(ai_ls[-1])

ai_fin = list()
for ai in ai_unique:
  if not seen[ai]:
    ai_fin.append(ai)

print(len(ai_fin))