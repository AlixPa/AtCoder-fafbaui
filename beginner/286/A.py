import sys
def IIS(): return map(int, input().split())
def SIS(): return input().split()
def II(): return int(input())
def SI(): return input()
def FIS(): return map(float, input().split())
def FI(): return float(input())
sys.setrecursionlimit(10**8)


(n, p, q, r, s) = IIS()
A = IIS()
AN = list()
AN.append(0)
for a in A:
  AN.append(a)
BN = ""
dif = q - p + 1
i = 1
while i < p:
  #print(AN[i])
  BN += str(AN[i]) + " "
  i += 1
for j in range(dif):
  #print(AN[r+j])
  BN += str(AN[r+j]) + " "
  i += 1
while i < r:
  #print(AN[i])
  BN += str(AN[i]) + " "
  i += 1
for j in range(dif):
  #print(AN[p+j])
  BN += str(AN[p+j]) + " "
  i += 1
while i <= n:
  #print(AN[i])
  BN += str(AN[i]) + " "
  i += 1

print(BN[:-1])