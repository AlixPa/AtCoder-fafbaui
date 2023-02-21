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
  '''
  Simple depht first search of a graph def by its vertices
  Set #here the modifications you want it to do
  '''
  if u.visited :
    #here return
    return
  list_pile = [u]
  while True:
    if len(list_pile) == 0:
      break
    v = list_pile.pop()
    if v.visited:
      continue
    #here, we are "in the current vertex"
    v.visit()
    linked = v.get_linked()
    for vp in linked:
      list_pile.append(vp)
  #here return
  return
