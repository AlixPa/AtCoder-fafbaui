import sys, math
def IIS(): return map(int, input().split())
def SIS(): return input().split()
def II(): return int(input())
def SI(): return input()
def FIS(): return map(float, input().split())
def FI(): return float(input())
sys.setrecursionlimit(10**8)

n, m = IIS()
ai_ls = list()
bi_ls = list()
cj_ls = list()
dj_ls = list()

for _ in range(n):
  a, b = IIS()
  ai_ls.append(a)
  bi_ls.append(b)
for _ in range(m):
  c, d = IIS()
  cj_ls.append(c)
  dj_ls.append(d)

checkpoint_ls = list()
for i in range(n):
  a = ai_ls[i]
  b = bi_ls[i]
  dist_min = math.inf
  index_min = -1
  for j in range(m):
    c = cj_ls[j]
    d = dj_ls[j]
    dist = abs(a - c) + abs(b - d)
    if dist < dist_min:
      dist_min = dist
      index_min = j
  checkpoint_ls.append(index_min + 1)

for checkpoint in checkpoint_ls:
  print(checkpoint)