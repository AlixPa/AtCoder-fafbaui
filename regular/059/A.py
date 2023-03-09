import sys
def IIS(): return map(int, input().split())
def SIS(): return input().split()
def II(): return int(input())
def SI(): return input()
def FIS(): return map(float, input().split())
def FI(): return float(input())
sys.setrecursionlimit(10**8)

n = II()
ls_ai = list(IIS())

moyenne = sum(ls_ai)//len(ls_ai)
sum1 = 0
sum2 = 0
for ai in ls_ai:
  sum1 += (ai-moyenne)*(ai-moyenne)
  sum2 += (ai-(moyenne+1))*(ai-(moyenne+1))
print(min(sum1, sum2))