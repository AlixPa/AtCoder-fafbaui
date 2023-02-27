import sys
def IIS(): return map(int, input().split())
def SIS(): return input().split()
def II(): return int(input())
def SI(): return input()
def FIS(): return map(float, input().split())
def FI(): return float(input())
sys.setrecursionlimit(10**8)

n = II()
ai_ls = list(IIS())

ai_ls.sort()

sum_comfort = 0
if len(ai_ls) < 2:
  print(sum_comfort)
  sys.exit(0)

sum_comfort += ai_ls[-1]
ai_ls = ai_ls[::-1][1:]
for i in range((n-2)//2):
  sum_comfort += 2*ai_ls[i]
if (n-2)%2 != 0:
  sum_comfort += ai_ls[((n-2)//2)]

print(sum_comfort)