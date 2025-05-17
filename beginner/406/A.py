# import copy
# import itertools
# import math
# from bisect import insort, insort_left, insort_right
# from collections import defaultdict, deque
# from heapq import heapify, heappop, heappush
import sys

sys.setrecursionlimit(10**8)

a, b, c, d = map(int, input().split())
print("Yes" if c < a or (c == a and d <= b) else "No")
