import sys
def IIS(): return map(int, input().split())
def SIS(): return input().split()
def II(): return int(input())
def SI(): return input()
def FIS(): return map(float, input().split())
def FI(): return float(input())
sys.setrecursionlimit(10**8)

n = II()
s = SI()

pos = (0, 0)
passed_dt = dict()
passed_dt[pos] = 0
crossed = False

def getPos(cur_pos, new_direction):
  x, y = cur_pos
  if new_direction == "R":
    new_pos = (x+1, y)
  elif new_direction == "L":
    new_pos = (x-1, y)
  elif new_direction == "U":
    new_pos = (x, y+1)
  elif new_direction == "D":
    new_pos = (x, y-1)
  return new_pos

for direction in s:
  pos = getPos(pos, direction)
  try:
    saw = passed_dt[pos]
    crossed = True
  except:
    passed_dt[pos] = 0
  if crossed:
    print("Yes")
    sys.exit(0)

print("No")