import sys
def IIS(): return map(int, input().split())
def SIS(): return input().split()
def II(): return int(input())
def SI(): return input()
def FIS(): return map(float, input().split())
def FI(): return float(input())
sys.setrecursionlimit(10**8)

n = II()
st_x = set()
dt_x = dict()
dt_y = dict()

for _ in range(n):
  x, y = IIS()
  st_x.add(x)
  if x not in dt_x:
    dt_x[x] = set()
  if y not in dt_y:
    dt_y[y] = set()
  dt_x[x].add(y)
  dt_y[y].add(x)
ls_x = list(st_x)
ls_x.sort()

nb_sq = 0
for x1 in ls_x:
  st_y_cur = dt_x[x1]
  for y1 in st_y_cur:
    for x2 in dt_y[y1]:
      if x2 <= x1:
        continue
      for y2 in dt_x[x2]:
        if y2 <= y1:
          continue
        if y2 in dt_x[x1]:
          nb_sq += 1

print(nb_sq)