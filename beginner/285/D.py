import sys
def IIS(): return map(int, input().split())
def SIS(): return input().split()
def II(): return int(input())
def SI(): return input()
def FIS(): return map(float, input().split())
def FI(): return float(input())
sys.setrecursionlimit(10**8)

class vertex:
  def __init__(self):
    self.links = None
    self.start = False
    self.visited = False

n = II()
graph = [vertex() for _ in range(n)]
dict_mem_bef = dict()
dict_mem_aft = dict()
set_cmpt = set()

for i in range(n):
  s,t = SIS()
  # i got s before
  dict_mem_bef[s] = i
  # i wants t
  dict_mem_aft[i] = t
  set_cmpt.add(t)

# 2 to same dot
if len(set_cmpt) < n:
  print("No")
  sys.exit(0)

# add links
for i in range(n):
  try:
    # i wants dict_mem_aft[i]
    wanted = dict_mem_aft[i]
    # wanted is in k vertex
    k = dict_mem_bef[wanted]
    graph[i].links = graph[k]
    graph[k].is_parent = False
  except:
    continue

# detect cycles
def dfs(u):
  # get next
  v = u.links
  # if get out of graph osef
  if v == None:
    return
  # if next is start, means we've done a cycle
  if v.start:
    print("No")
    sys.exit(0)
  # avoid further researchs if already visited
  if v.visited:
    return
  v.visited = True
  # go to next
  dfs(v)

for u in graph:
  if not u.visited:
    # set the starting point
    u.start = True
    dfs(u)
    # erase starting point in case of father start later
    u.start = False

print("Yes")

