def groupList(ls):
  '''
  Take a sorted list, return two lists made of groupes suites and number of elements in suite, and sum for the second
  [1, 2, 4, 6, 7, 8] => ( [(1, 2), (4, 1), (6, 3)], [(1, 2), (4, 3), (6, 6)] )
  '''
  #ls.sort()
  if len(ls) == 0:
    return (list(), list())
  elif len(ls) == 1:
    return ([(ls[0], 1)], [ls[0], 1])
  saved = ls[0]
  seen = 1
  seen_sum = 0
  ret_ls = list()
  ret_ls_sum = list()
  for e in (ls[1:] + [0]):
    if e == saved + seen:
      seen += 1
    else:
      seen_sum += seen
      ret_ls.append((saved, seen))
      ret_ls_sum.append((saved, seen_sum))
      saved = e
      seen = 1
  return (ret_ls, ret_ls_sum)

