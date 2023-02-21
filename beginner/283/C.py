s = input()

cpt_z = 0
n = 0
for k in s :
  if int(k) != 0 :
    n += 1
    if cpt_z == 1:
      cpt_z = 0
      n += 1
  else :
    if cpt_z == 0 :
      cpt_z += 1
    else :
      cpt_z = 0
      n += 1
n += cpt_z

print(n)