# import copy
# import itertools
import math

# from bisect import insort, insort_left, insort_right
# from collections import defaultdict, deque
# from heapq import heapify, heappop, heappush
import sys

sys.setrecursionlimit(10**8)

t = int(input())
MOD = 998244353


def get_count(n_bit, n_bit_allowed, offset):
    if n_bit < n_bit_allowed or n_bit == 0:
        return 0
    sm = sum([pow(2, i, MOD) for i in range(n_bit)]) % MOD
    cb = (math.comb(n_bit, n_bit_allowed) * n_bit_allowed // n_bit) % MOD
    return (cb * sm) % MOD + ((math.comb(n_bit, n_bit_allowed) % MOD) * offset) % MOD


for _ in range(t):
    n, k = map(int, input().split())
    cnt = 0
    offset = 0
    while n and k:
        cnt += get_count(n.bit_length() - 1, k, offset)
        cnt %= MOD
        k -= 1
        new_offset = pow(2, n.bit_length() - 1)
        n -= new_offset
        offset = (offset + new_offset) % MOD
    if k == 0:
        cnt = (cnt + offset) % MOD
    print(cnt)
