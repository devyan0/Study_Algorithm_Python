"""
https://www.acmicpc.net/problem/3079
calculate optimal initial r
"""
from functools import reduce
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
times = [int(input()) for _ in range(N)]

can_handle = lambda t_given: M <= sum([t_given//t for t in times])

mult = lambda arr: reduce(lambda x, y: x*y, arr)

MAX_N = 100_000
# overflow error
# https://help.acmicpc.net/judge/rte/OverflowError
MAX_PEOPLE = int(mult(times) / sum(times) * MAX_N)  # overflow
MAX_PEOPLE = min(MAX_PEOPLE, sys.maxsize-1)         # overflow
print(MAX_PEOPLE)
l, r = 1, MAX_PEOPLE+1
while l < r:
    mid = (l+r)//2
    if can_handle(mid):
        r = mid
    else:
        l = mid + 1

print(l)
