import sys
def IIS(): return map(int, input().split())
def SIS(): return input().split()
def II(): return int(input())
def SI(): return input()
def FIS(): return map(float, input().split())
def FI(): return float(input())
sys.setrecursionlimit(10**8)

n, m = IIS()
ls_sets = [set()]

for _ in range(m):
  _ = IIS()
  ls_sets.append(set(IIS()))

def isIn(k, set_num):
  return (k%(pow(2, set_num))) >= (pow(2, set_num - 1))

ls_chooses = [set()]
for k in range(1, pow(2,m)):
  tmp_set = set()
  for set_num in range(1, m+1):
    if isIn(k, set_num):
      tmp_set = tmp_set.union(ls_sets[set_num])
  ls_chooses.append(tmp_set)

count = 0
for k in range(1, pow(2,m)):
  if len(ls_chooses[k]) == n:
    count += 1

print(count)