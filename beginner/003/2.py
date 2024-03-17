import sys
def SI(): return input()

s1 = SI()
s2 = SI()

st_at = {"a", "t", "c", "o", "d", "e", "r"}

for i in range(len(s1)):
  if s1[i] != s2[i]:
    if (s1[i] == "@" and s2[i] != "@" and s2[i] not in st_at) or (s2[i] == "@" and s1[i] != "@" and s1[i] not in st_at) or (s1[i] != "@" and s2[i] != "@" and s1[i] != s2[i]):
      print("You will lose")
      sys.exit(0)
print("You can win")