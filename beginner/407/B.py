# import copy
# import itertools
# import math
# from bisect import insort, insort_left, insort_right
# from collections import defaultdict, deque
# from heapq import heapify, heappop, heappush
import sys

sys.setrecursionlimit(10**8)

x, y = map(int, input().split())
cnt = 0
tot = 0
for i in range(1, 7):
    for j in range(1, 7):
        if i + j >= x or abs(i - j) >= y:
            cnt += 1
        tot += 1
print(cnt / tot)
