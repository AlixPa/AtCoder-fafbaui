import sys
def IIS(): return map(int, input().split())
def SIS(): return input().split()
def II(): return int(input())
def SI(): return input()
def FIS(): return map(float, input().split())
def FI(): return float(input())
sys.setrecursionlimit(10**8)

n = II()
s = SI()
t = SI()

s_ls = [0]*26
t_ls = [0]*26

for si in s:
  s_ls[ord(si) - ord("a")] += 1
for ti in t:
  t_ls[ord(ti) - ord("a")] += 1

for (nb_s, nb_t) in zip(s_ls, t_ls):
  if nb_s != nb_t:
    print(-1)
    sys.exit(0)

s = s[::-1]
t = t[::-1]

i_s = 0
for ti in t:
  if ti == s[i_s]:
    i_s += 1

print(n - i_s)