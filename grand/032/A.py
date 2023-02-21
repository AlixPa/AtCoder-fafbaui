import sys
def IIS(): return map(int, input().split())
def SIS(): return input().split()
def II(): return int(input())
def SI(): return input()
def FIS(): return map(float, input().split())
def FI(): return float(input())
sys.setrecursionlimit(10**8)

n = II()
bi_ls = list(IIS())

def get_pos_max_left(cur_ls):
  max_max = 0
  index_max = -1
  for i in range(len(cur_ls)):
    if cur_ls[i] > max_max:
      max_max = cur_ls[i]
      index_max = i
  return index_max

is_played = [False]*(n + 1)
got_played = [0]*(n + 1)

try:
  for i in range(n):
    index_max = get_pos_max_left(bi_ls)
    left_max = bi_ls[index_max]
    dif = (index_max + 1) - left_max
    played_at_local = len(bi_ls) - dif
    played_at = 0
    match_played_at_local = 0
    while True:
      if match_played_at_local == played_at_local:
        break
      played_at += 1
      if not is_played[played_at]:
        match_played_at_local += 1
    is_played[played_at] = True
    got_played[played_at] = left_max
    bi_ls.pop(index_max)
  for play in got_played[1:]:
    print(play)
except:
  print(-1)