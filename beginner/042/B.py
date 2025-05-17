# import copy
# import itertools
# import math
# from bisect import insort, insort_left, insort_right
# from collections import defaultdict, deque
# from heapq import heapify, heappop, heappush
import sys

sys.setrecursionlimit(10**8)

n, l = map(int, input().split())
ss = [input() for _ in range(n)]

ss.sort()
for s in ss:
    print(s, end="")

## Quel crétin lol
# order = list()
# fifo = deque()
# # (index of search, string to search)
# fifo.append((0, [i for i in range(n)]))
# placed = set()
# while fifo:
#     pos, ls_search = fifo.pop()
#     if pos >= l:
#         order.extend(ls_search)
#         continue
#     letters = set()
#     for i in ls_search:
#         letters.add(ss[i][pos])
#     if len(letters) == 1:
#         fifo.append((pos + 1, ls_search))
#     else:
#         min_letter = min(letters)
#         ls_min = [i for i in ls_search if ss[i][pos] == min_letter]
#         ls_not_min = [i for i in ls_search if ss[i][pos] != min_letter]
#         fifo.append((pos, ls_not_min))
#         fifo.append((pos + 1, ls_min))

# for o in order:
#     print(ss[o], end="")
