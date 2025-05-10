# import copy
# import itertools
# import math
# from bisect import insort, insort_left, insort_right
# from collections import defaultdict, deque
# from heapq import heapify, heappop, heappush
import sys

sys.setrecursionlimit(10**8)

r, x = map(int, input().split())

if x == 1:
    print("Yes" if r >= 1600 and r <= 2999 else "No")
else:
    print("Yes" if r >= 1200 and r <= 2399 else "No")
