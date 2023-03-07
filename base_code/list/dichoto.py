def dichoSearch(k, ls):
  '''
  Take a sorted listed and an item, return the indice of the greater smaller int of the item (-1 if the item is smaller than all)
  (3, [1, 4, 7]) => 0
  (5, [0, 1, 2, 3, 10]) => 3
  '''
  #ls.sort()
  if len(ls) == 0:
    return -1
  if k < ls[0]:
    return -1
  left = 0
  right = len(ls) - 1
  while True:
    dif = right - left
    if dif == 0:
      return left
    center = left + (dif+1)//2
    if ls[center] <= k:
      left = center
    else:
      right = center - 1