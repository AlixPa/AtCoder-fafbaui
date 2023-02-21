import sys
def IIS(): return map(int, input().split())
def SIS(): return input().split()
def II(): return int(input())
def SI(): return input()
def FIS(): return map(float, input().split())
def FI(): return float(input())
sys.setrecursionlimit(10**8)

_ = II()
ls_climbs = list(IIS())
m = II()
ls_trap = list(IIS())
x = II()

traps = [False for _ in range(x+1)]
for trap in ls_trap:
  traps[trap] = True

stairs = [False for _ in range(x+1)]
stairs[0] = True

for step in range(x+1):
  if traps[step]:
    continue
  if not stairs[step]:
    continue
  for climb in ls_climbs:
    next_step = step+climb
    if next_step > x:
      continue
    stairs[next_step] = True

if stairs[x]:
  print("Yes")
else:
  print("No")