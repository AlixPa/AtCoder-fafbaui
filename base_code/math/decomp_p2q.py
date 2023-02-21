def decomp_pkq(n, k):
  '''
  Return (p,q) as a tuple, where n=(p**2)*q
  Decomposition MUST be possible, else it will f**** up
  '''
  r = int(n**(1/(k+1)))
  for i in range(2, r+1):
    if n%i == 0:
      if n%(i**k) == 0:
        return (i, n//(i**k))
      else:
        return (int((n//i)**(1/k)), i)