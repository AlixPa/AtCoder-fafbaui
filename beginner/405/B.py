# import copy
# import itertools
# import math
# from bisect import insort, insort_left, insort_right
# from collections import defaultdict, deque
# from heapq import heapify, heappop, heappush
import sys

sys.setrecursionlimit(10**8)

n, m = map(int, input().split())
ls_a = list(map(int, input().split()))

for i in range(0, n):
    is_full = True
    for j in range(1, m + 1):
        if j not in ls_a[: i + 1]:
            is_full = False
            break
    if is_full:
        print(n - i)
        sys.exit(0)
print(0)
