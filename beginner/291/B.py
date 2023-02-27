import sys
def IIS(): return map(int, input().split())
def SIS(): return input().split()
def II(): return int(input())
def SI(): return input()
def FIS(): return map(float, input().split())
def FI(): return float(input())
sys.setrecursionlimit(10**8)

n = II()
judges_ls = list(IIS())
judges_ls.sort()

tot = 0
for note in judges_ls[n:-n]:
  tot += note

print(float(tot)/float(3*n))