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


def get_outers(x: int, y: int, dt_corres: dict[tuple[int, int], int]) -> list[int]:
    return [
        dt_corres[(xp, yp)]
        for xp, yp in [
            (x - 1, y - 1),
            (x - 1, y),
            (x, y - 1),
            (x, y + 1),
            (x + 1, y),
            (x + 1, y + 1),
        ]
        if (xp, yp) in dt_corres
    ]


nb_nodes: int = II()
edges: dict[int, list[int]] = dict()
dt_corres: dict[tuple[int, int], int] = dict()
x, y = 0, 0
nb = 0
for _ in range(nb_nodes):
    x, y = IIS()
    dt_corres[(x, y)] = nb
    edges[nb] = list()
    for node in get_outers(x, y, dt_corres):
        edges[node].append(nb)
        edges[nb].append(node)
    nb += 1

seen = [False] * nb_nodes
added = [False] * nb_nodes
nb_comp = 0
for first_node in range(nb_nodes):
    if seen[first_node]:
        continue
    fifo: deque = deque()
    fifo.append(first_node)
    nb_comp += 1
    seen[first_node] = True
    added[first_node] = True
    while fifo:
        cur = fifo.pop()
        for node in edges[cur]:
            if added[node] or seen[node]:
                continue
            fifo.append(node)
            added[node] = True
        seen[cur] = True

print(nb_comp)
