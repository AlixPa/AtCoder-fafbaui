## We are here using a few assertions (quite easy to demonstrate),
### First assertion: dist("1 2 3", "1 3 2") == dist("2 3", "3 2")
### Second assertion: by naming "min_perm("X1 X2 X3 ... Xk")" the first k-permutation by lexicographic order (example: 1234, 123456, 12345678...)
#### We can asses that dist("1" + min_perm("X1 X2 ... Xk"), "4" + min_perm("X1 X2 ... Xk")) == (4 - 1)*factorial(k)
### Third assertion: we can conclude, (WITH p < q!!), that dist(p, q) = dist(min_perm(p), min_perm(q)) + dist(min_perm(q), q) - dist(min_perm(p), p)
import sys
def IIS(): return map(int, input().split())
def SIS(): return input().split()
def II(): return int(input())
def SI(): return input()
def FIS(): return map(float, input().split())
def FI(): return float(input())
sys.setrecursionlimit(10**8)

n = II()
p = list(IIS())
q = list(IIS())

def facto(k):
  if k <= 1:
    return 1
  return k*facto(k-1)

def distRec(r, s):
  ## Assertion 1: r & s have non ordered continuous number lists [1, 3, 2] for example, not [1, 4, 2], missing the "3" in the second
  ## Assertion 2: r < s
  if len(r) == 0:
    return 0
  # get distance indice 0 for fact mult, "from r to s"
  dist_first = s[0] - r[0]
  # make next r continuous
  next_r = r[1:]
  for i in range(len(next_r)):
    if next_r[i] > r[0]:
      next_r[i] -= 1
  # make next s continuous
  next_s = s[1:]
  for i in range(len(next_s)):
    if next_s[i] > s[0]:
      next_s[i] -= 1
  # if same, then distance is same as next
  if dist_first == 0:
    return distRec(next_r, next_s)
  # get each list "min"
  next_r_min = next_r.copy()
  next_r_min.sort()
  next_s_min = next_s.copy()
  next_s_min.sort()
  
  return dist_first*facto(len(next_r)) + distRec(next_s_min, next_s) - distRec(next_r_min, next_r)

for (pi, qi) in zip(p, q):
  if pi < qi:
    print(abs(distRec(p, q)))
    sys.exit(0)
  if pi > qi:
    print(abs(distRec(q, p)))
    sys.exit(0)

print(0)