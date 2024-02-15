import sys
def IIS(): return map(int, input().split())
def SIS(): return input().split()
def II(): return int(input())
def SI(): return input()
def FIS(): return map(float, input().split())
def FI(): return float(input())
sys.setrecursionlimit(10**8)

n = II()
ls_pt = list()
for _ in range(n):
  x, y = IIS()
  ls_pt.append((x,y))
ls_pt.sort()

pq_dt = dict()
for (pt1, i) in zip(ls_pt, range(n)):
  x1, y1 = pt1
  for (pt2, j) in zip(ls_pt[i+1:], range(i+1, n)):
    x2, y2 = pt2
    #if y1 > y2:
      #continue
    p = x2 - x1
    q = y2 - y1
    nb_step = 2
    net_tmp = [i, j]
    for (pt3, k) in zip(ls_pt[j+1:], range(j+1, n)):
      x3, y3 = pt3
      #if y2 > y3:
        #continue
      dx = x3 - x1
      dy = y3 - y1
      if dx == nb_step*p and dy == nb_step*q:
        net_tmp.append(k)
        nb_step += 1
    if (p, q) not in pq_dt:
      pq_dt[(p, q)] = [net_tmp]
      continue
    skip = False
    for net in pq_dt[(p, q)]:
      if net[-1] == net_tmp[-1]:
        skip = True
        break
    if not skip:
      pq_dt[(p, q)].append(net_tmp)

max_sum = 0
for pq in pq_dt:
  ls_ls = pq_dt[pq]
  tmp_sum = 0
  for ls in ls_ls:
    tmp_sum += len(ls) -1
  if tmp_sum > max_sum:
    max_sum = tmp_sum

print(n - max_sum)
