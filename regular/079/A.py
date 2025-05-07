import copy
import itertools
import math
import sys
from bisect import insort, insort_left, insort_right
from collections import defaultdict, deque
from heapq import heapify, heappop, heappush


def IIS():
    return map(int, input().split())


def LIIS():
    return list(IIS())


def SIIS():
    return set(IIS())


def SIS():
    return input().split()


def II():
    return int(input())


def SI():
    return input()


def FIS():
    return map(float, input().split())


def FI():
    return float(input())


sys.setrecursionlimit(10**8)

n, m = IIS()
edges: dict[int, set[int]] = dict()

for _ in range(m):
    a, b = IIS()
    if a not in edges:
        edges[a] = set()
    if b not in edges:
        edges[b] = set()
    edges[a].add(b)
    edges[b].add(a)

if not 1 in edges:
    print("IMPOSSIBLE")
    sys.exit(0)

one_step = edges[1]
two_steps: set[int] = set()
for i in one_step:
    two_steps = two_steps.union(two_steps, edges[i])

if n in two_steps:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")
