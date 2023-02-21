t = int(input())

tab = []

for i in range(t) :
  _ = input()
  tab.append([int(n) for n in input().split()])

for i in range(t) :
  s_tab = tab[i]
  n = 0
  for k in s_tab :
    if k%2 != 0 :
      n += 1
  print(n)