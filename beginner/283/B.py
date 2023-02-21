n = int(input())
an = [int(ai) for ai in input().split()]
q = int(input())
qn = []
for i in range(q) :
  qn.append([int(qi) for qi in input().split()])

for qi in qn :
  if qi[0] == 2 :
    print(an[qi[1] - 1])
  else :
    an[qi[1] -1] = qi[2]