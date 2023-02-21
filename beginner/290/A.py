import sys
def IIS(): return map(int, input().split())
def SIS(): return input().split()
def II(): return int(input())
def SI(): return input()
def FIS(): return map(float, input().split())
def FI(): return float(input())
sys.setrecursionlimit(10**8)

n, m = IIS()
ls_scores = list(IIS())
ls_solved = list(IIS())

score = 0

for solved in ls_solved:
  score += ls_scores[solved - 1]

print(score)