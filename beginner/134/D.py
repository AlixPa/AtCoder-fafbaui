# import copy
# import itertools
# import math
# from bisect import insort, insort_left, insort_right
# from collections import defaultdict, deque
# from heapq import heapify, heappop, heappush
import sys

sys.setrecursionlimit(10**8)

## box[i] depends on box[2*i], box[3*i], etc
# in fact we want (sum(box[i], box[2*i], ...) %2 = ai %2)
# which means box[i] = (sum(box[2*i], box[3*i], ...) + ai) % 2
# then ofc, we need to fill box[n] before box[n-1] etc

n = int(input())
ais = list(map(int, input().split()))
boxes = [0] * n

for i in range(n, 0, -1):
    s = 0
    j = i
    while j <= n:
        s += boxes[j - 1]
        j += i
    boxes[i - 1] = (s + ais[i - 1]) % 2

print(sum(boxes))
to_print = [str(i + 1) for i in range(n) if boxes[i]]
if to_print:
    print(" ".join(to_print))
