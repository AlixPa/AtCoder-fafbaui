import sys
def IIS(): return map(int, input().split())
def SIS(): return input().split()
def II(): return int(input())
def SI(): return input()
def FIS(): return map(float, input().split())
def FI(): return float(input())
sys.setrecursionlimit(10**8)

n = II()

left = 1
right = n//2
prev_right = n
for _ in range(20):
  if left == prev_right:
    break
  print(f"? {left} {right} {1} {n}", flush=True)
  t = II()
  if t == (right-left) + 1:
    left = right + 1
    right = prev_right
  else:
    prev_right = right
  right = left + (right-left-1)//2

up = 1
down = n//2
prev_down = n
for _ in range(20):
  if up == prev_down:
    break
  print(f"? {1} {n} {up} {down}", flush=True)
  t = II()
  if t == (down-up) + 1:
    up = down + 1
    down = prev_down
  else:
    prev_down = down
  down = up + (down-up-1)//2

print(f"! {left} {up}", flush=True)