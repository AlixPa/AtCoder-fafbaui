import sys
def IIS(): return map(int, input().split())
def SIS(): return input().split()
def II(): return int(input())
def SI(): return input()
def FIS(): return map(float, input().split())
def FI(): return float(input())
sys.setrecursionlimit(10**8)

tree = [set() for i in range(16)]
for i in range(8):
  tree[i].add(2*i)
  tree[i].add(2*i + 1)

a,b = IIS()

if (a in tree[b]) or (b in tree[a]):
  print("Yes")
else:
  print("No")