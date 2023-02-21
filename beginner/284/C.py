def iis():
  return map(int, input().split())

def sis():
  return input().split()

def ii():
  return int(input())

def si():
  return input()

def fis():
  return map(float, input().split())

def fi():
  return float(input())

class vertex:
  def __init__(self, number=None, linked=None):
    self.number = 0
    self.links = set()
    self.visited = False
    if number is not None:
      self.number = number
    if linked is not None:
      for v in linked:
        self.links.add(v)

  def add_link(self, v):
    self.links.add(v)
    v.single_side_add_link(self)

  def single_side_add_link(self, v):
    self.links.add(v)

  def change_number(self, number):
    self.number = number

  def visit(self):
    self.visited = True

  def get_linked(self):
    return self.links

def dfs(u):
  if u.visited :
    return
  list_pile = [u]
  while True:
    if len(list_pile) == 0:
      break
    v = list_pile.pop()
    if v.visited:
      continue
    v.visit()
    linked = v.get_linked()
    for vp in linked:
      list_pile.append(vp)
  return


n,m = iis()

vertices = [vertex() for i in range(n)]

for i in range(m):
  u,v = iis()
  vertices[u-1].add_link(vertices[v-1])

nb = 0
for v in vertices:
  if not v.visited:
    nb +=1
    dfs(v)

print(nb)