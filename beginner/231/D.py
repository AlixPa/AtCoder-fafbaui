import sys
def IIS(): return map(int, input().split())
def SIS(): return input().split()
def II(): return int(input())
def SI(): return input()
def FIS(): return map(float, input().split())
def FI(): return float(input())
sys.setrecursionlimit(10**8)

n, m = IIS()

seen = [False for _ in range(n+1)]
neighboors = [list() for _ in range(n+1)]

for _ in range(m):
  a, b = IIS()
  neighboors[a].append(b)
  neighboors[b].append(a)

for neighs in neighboors:
  if len(neighs) > 2:
    print("No")
    sys.exit(0)

def dfsSpe(last, current):
  global seen
  global neighboors
  if seen[current]:
    print("No")
    sys.exit(0)
  seen[current] = True
  neighs = neighboors[current]
  if len(neighs) == 1:
    if neighs[0] == last:
      return 0
    else:
      return dfsSpe(current, neighs[0])
  else:
    if neighs[0] == last:
      return dfsSpe(current, neighs[1])
    else:
      return dfsSpe(current, neighs[0])

for i in range(1, n+1):
  if not seen[i]:
    seen[i] = True
    for neigh in neighboors[i]:
      k = dfsSpe(i, neigh)

print("Yes")