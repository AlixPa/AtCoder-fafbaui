def uniquesNumbersInLs(ls):
  '''
  Returns the list of unique numbers
  [1, 2, 2, 3, 4, 4, 4] => [1, 3]
  '''
  #ls.sort()
  if len(ls) <= 1:
    return ls
  new_ls = list()
  last  = ls[0]
  nb_last = 1
  for k in ls[1:]:
    if k != last:
      if nb_last == 1:
        new_ls.append(last)
      nb_last = 1
      last = k
    else:
      nb_last += 1
  if ls[-1] != ls[-2]:
    new_ls.append(ls[-1])
  return new_ls

def lsOfLsNonUnique(ls):
  '''
  Returns sub lists each containing the lists of non-unique numbers
  [1, 2, 2, 3, 4, 4, 4] => [[2, 2], [4, 4, 4]]
  '''
  ls = ls.copy()
  #ls.sort()
  if len(ls) <= 1:
    return [ls]
  last = ls[0]
  ls_of_ls = list()
  tmp_ls = [ls[0]]
  for k in ls[1:]:
    if k == last:
      tmp_ls.append(k)
    else:
      last = k
      if len(tmp_ls) > 1:
        ls_of_ls.append(tmp_ls)
      tmp_ls = [k]
  if len(tmp_ls) > 1:
    ls_of_ls.append(tmp_ls)
  return ls_of_ls