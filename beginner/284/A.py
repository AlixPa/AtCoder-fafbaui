n = int(input())
tab = []
for i in range(n) :
  tab.append(input())

for i in range(n) :
  print(tab[-(i+1)])