# import copy
# import itertools
# import math
# from bisect import insort, insort_left, insort_right
# from collections import defaultdict, deque
# from heapq import heapify, heappop, heappush
import sys

sys.setrecursionlimit(10**8)

n, k = map(int, input().split())
lsa = list(map(int, input().split()))
v = 1
max_v = 10**k - 1
for a in lsa:
    v *= a
    if v > max_v:
        v = 1
print(v)
