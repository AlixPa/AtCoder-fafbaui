import sys, math, copy, itertools
from collections import deque, defaultdict
from heapq import heappop, heappush, heapify
def IIS(): return map(int, input().split())
def LIIS(): return list(IIS())
def SIIS(): return set(IIS())
def SIS(): return input().split()
def II(): return int(input())
def SI(): return input()
def FIS(): return map(float, input().split())
def FI(): return float(input())
sys.setrecursionlimit(10**8)

def verifPlace(grid, i, j, block):
  r, c = block[0]
  if i+r > 4 or j+c > 4:
    return False
  for k in range(r):
    for l in range(c):
      if grid[i+k][j+l] == 1 and block[1][k][l] == "#":
        return False
  return True

def place(grid, i, j, block):
  new_grid = copy.deepcopy(grid)
  r, c = block[0]
  for k in range(r):
    for l in range(c):
      if block[1][k][l] == "#":
        new_grid[i+k][j+l] = 1
  return new_grid

tmp = list()
for _ in range(3):
  tmp_f = list()
  for _ in range(4):
    s = SI()
    tmp_f.append(s)
  tmp.append(tmp_f)

nb_pin = 0
for i in range(3):
  for j in range(4):
    for k in range(4):
      if tmp[i][j][k] == "#":
        nb_pin += 1
if nb_pin != 16:
  print("No")
  sys.exit(0)

f_blocks = list()
for i in range(3):
  for start_r in range(4):
    if "#" in tmp[i][start_r]:
      break
  for end_r in range(3, -1, -1):
    if "#" in tmp[i][end_r]:
      break
  for start_c in range(4):
    if "#" in [tmp[i][c][start_c] for c in range(4)]:
      break
  for end_c in range(3, -1, -1):
    if "#" in [tmp[i][c][end_c] for c in range(4)]:
      break
  block = list()
  for r in range(start_r, end_r+1):
    tmp_r = list()
    for c in range(start_c, end_c+1):
      tmp_r.append(tmp[i][r][c])
    block.append(tmp_r)
  f_blocks.append(block)

f_blocks_mult = list()
for i in range(3):
  size_reg = [len(f_blocks[i]), len(f_blocks[i][0])]
  size_flip = [size_reg[-1], size_reg[0]]
  f1 = list()
  for r in range(size_reg[0]):
    tmp_c = list()
    for c in range(size_reg[1]):
      tmp_c.append(f_blocks[i][r][c])
    f1.append(tmp_c)
  f2 = list()
  for c in range(size_reg[1]):
    tmp_c = list()
    for r in range(size_reg[0]-1, -1, -1):
      tmp_c.append(f_blocks[i][r][c])
    f2.append(tmp_c)
  f3 = list()
  for r in range(size_reg[0]-1, -1, -1):
    tmp_c = list()
    for c in range(size_reg[1]-1, -1, -1):
      tmp_c.append(f_blocks[i][r][c])
    f3.append(tmp_c)
  f4 = list()
  for c in range(size_reg[1]-1, -1, -1):
    tmp_c = list()
    for r in range(size_reg[0]):
      tmp_c.append(f_blocks[i][r][c])
    f4.append(tmp_c)
  tmp_f = list()
  tmp_f.append([size_reg, f1])
  tmp_f.append([size_flip, f2])
  tmp_f.append([size_reg, f3])
  tmp_f.append([size_flip, f4])
  f_blocks_mult.append(tmp_f)

grid = [[0 for _ in range(4)] for _ in range(4)]
for i1, j1, f1 in itertools.product(range(4), range(4), range(4)):
  if verifPlace(grid, i1, j1, f_blocks_mult[0][f1]):
    grid_f1 = place(grid, i1, j1, f_blocks_mult[0][f1])
    for i2, j2, f2 in itertools.product(range(4), range(4), range(4)):
      if verifPlace(grid_f1, i2, j2, f_blocks_mult[1][f2]):
        grid_f2 = place(grid_f1, i2, j2, f_blocks_mult[1][f2])
        for i3, j3, f3 in itertools.product(range(4), range(4), range(4)):
          if verifPlace(grid_f2, i3, j3, f_blocks_mult[2][f3]):
            print("Yes")
            sys.exit(0)
print("No")