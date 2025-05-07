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

s, q = SI(), II()

rev = False
queue = deque()
for c in s:
    queue.append(c)

for _ in range(q):
    inp = SIS()
    if inp[0] == "1":
        rev = not rev
    else:
        if (inp[1] == "1" and not rev) or (inp[1] == "2" and rev):
            queue.appendleft(inp[2])
        else:
            queue.append(inp[2])

ret = list()
while queue:
    if not rev:
        c = queue.popleft()
    else:
        c = queue.pop()
    ret.append(c)

print("".join(ret))
