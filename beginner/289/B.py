import sys
def IIS(): return map(int, input().split())
def SIS(): return input().split()
def II(): return int(input())
def SI(): return input()
def FIS(): return map(float, input().split())
def FI(): return float(input())
sys.setrecursionlimit(10**8)

n, m = IIS()
ls_a = list()

ls_a = list(IIS())

tab_a = [i for i in range(1, n+1)]
for a in ls_a:
  tab_a.remove(a)

output = ""

prev_a = 0
for a in tab_a:
  for v in range(a, prev_a, -1):
    output += str(v) + " "
  prev_a = a

output = output[:-1]

print(output)