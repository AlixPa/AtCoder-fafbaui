# import copy
# import itertools
# import math
# from bisect import insort, insort_left, insort_right
# from collections import defaultdict, deque
# from heapq import heapify, heappop, heappush
import sys

sys.setrecursionlimit(10**8)

n = int(input())
ls_a = list(map(int, input().split()))

sums = [0] * n
sums[-1] = 0
for i in range(n - 2, -1, -1):
    sums[i] = sums[i + 1] + ls_a[i + 1]

tot = 0
for i in range(n):
    tot += ls_a[i] * sums[i]

print(tot)
