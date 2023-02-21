import sys
def IIS(): return map(int, input().split())
def SIS(): return input().split()
def II(): return int(input())
def SI(): return input()
def FIS(): return map(float, input().split())
def FI(): return float(input())
sys.setrecursionlimit(10**8)

s = SI()

if s == "zyxwvutsrqponmlkjihgfedcba":
  print(-1)
  sys.exit(0)

if len(s) < 26:
  ls_alphabet = [chr(l) for l in range(ord("a"), ord("z") + 1)]
  ls_s = [l for l in s]
  ls_s.sort()
  l_add = ""
  for (la, ls) in zip(ls_alphabet, ls_s):
    if la != ls:
      l_add = la
      break
  if l_add == "":
    l_add = ls_alphabet[len(s)]
  print(s + l_add)
  sys.exit(0)

s_inv = s[::-1]
indice_not_sorted = -27
ls_end_sorted = list()
for i in range(1, 27):
  indice_not_sorted = -i
  ls_end = [l for l in s_inv[:i]]
  ls_end_sorted = ls_end.copy()
  ls_end_sorted.sort()
  equals = True
  for (le, les) in zip(ls_end, ls_end_sorted):
    if le != les:
      equals = False
      break
  if not equals:
    break

new_letter = ""
for l in ls_end_sorted:
  if l > s[indice_not_sorted]:
    new_letter = l
    break

print(s[:indice_not_sorted] + new_letter)