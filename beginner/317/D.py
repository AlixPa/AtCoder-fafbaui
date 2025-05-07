# import copy
# import itertools
# import math
# from bisect import insort, insort_left, insort_right
# from collections import defaultdict, deque
# from heapq import heapify, heappop, heappush
import sys

sys.setrecursionlimit(10**8)

# knapsack
NB_ITEMS = int(input())
COSTS, VALUES = [0] * NB_ITEMS, [0] * NB_ITEMS
for i in range(NB_ITEMS):
    # TODO: cost and value calculation
    v_t, v_a, s = map(int, input().split())
    COSTS[i] = max(0, (v_t + v_a + 1) // 2 - v_t)
    VALUES[i] = s

TOTAL = sum(VALUES)
INF = sum(COSTS)
min_costs = [INF] * (2 * TOTAL)
min_costs[0] = 0
for cost, value in zip(COSTS, VALUES):
    for i in range(TOTAL - 1, -1, -1):
        min_costs[i + value] = min(min_costs[i + value], min_costs[i] + cost)

# TODO: define objective
OBJECTIVE = (TOTAL + 1) // 2
MIN_COST = min(min_costs[OBJECTIVE:])
print(MIN_COST)
