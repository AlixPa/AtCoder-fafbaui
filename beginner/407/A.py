# import copy
# import itertools
# import math
# from bisect import insort, insort_left, insort_right
# from collections import defaultdict, deque
# from heapq import heapify, heappop, heappush
import sys

sys.setrecursionlimit(10**8)

a, b = map(int, input().split())

dif = a / b - a // b
if dif < 0.5:
    print(a // b)
else:
    print(a // b + 1)
