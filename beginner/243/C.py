import sys
def IIS(): return map(int, input().split())
def SIS(): return input().split()
def II(): return int(input())
def SI(): return input()
def FIS(): return map(float, input().split())
def FI(): return float(input())
sys.setrecursionlimit(10**8)

n = II()
xy_ls = list()
y_dt = dict()
for _ in range(n):
  x, y = IIS()
  xy_ls.append((x,y))
  y_dt[f"{y}L"] = list()
  y_dt[f"{y}R"] = list()
s = SI()
y_st = set()
for ((x,y), direction) in zip(xy_ls, s):
  y_dt[f"{y}{direction}"].append(x)
  y_st.add(y)

for y in y_st:
  left_ls = y_dt[f"{y}L"]
  right_ls = y_dt[f"{y}R"]
  if len(left_ls) == 0 or len(right_ls) == 0:
    continue
  left_ls.sort()
  right_ls.sort()
  if left_ls[-1] >= right_ls[0]:
    print("Yes")
    sys.exit(0)

print("No")