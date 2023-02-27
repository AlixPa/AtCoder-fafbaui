import sys
def IIS(): return map(int, input().split())
def SIS(): return input().split()
def II(): return int(input())
def SI(): return input()
def FIS(): return map(float, input().split())
def FI(): return float(input())
sys.setrecursionlimit(10**8)

n, k = IIS()
r, s, p = IIS()
t = SI()

win_dt = {"r": "p", "s": "r", "p": "s"}
win_pt = {"r": r, "s": s, "p": p}
win_t = ""
for l in t:
  win_t += win_dt[l]
win_t = "0" + win_t

tot_pt = 0
for i in range(1, k+1):
  if i > n:
    break
  same_nb = 1
  hand = win_t[i]
  for j in range(1, (n+1//k)):
    if i + k*j > n:
      break
    if win_t[i + k*j] == hand:
      same_nb += 1
    else:
      tot_pt += ((same_nb+1)//2)*win_pt[hand]
      same_nb = 1
      hand = win_t[i + k*j]
  tot_pt += ((same_nb+1)//2)*win_pt[hand]

print(tot_pt)