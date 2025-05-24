# import copy
# import itertools
# import math
# from bisect import insort, insort_left, insort_right
# from collections import defaultdict, deque
# from heapq import heapify, heappop, heappush
import sys

sys.setrecursionlimit(10**8)

s = input()
ils = [int(e) for e in s]
cost = len(ils)
for i in range(1, len(ils)):
    if ils[i - 1] < ils[i]:
        ils[i - 1] += 10
    cost += ils[i - 1] - ils[i]
cost += ils[-1]
print(cost)
