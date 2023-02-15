"""
https://www.acmicpc.net/problem/3079
"""

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
times = [int(input()) for _ in range(N)]
NEED_TO_HANDLE = M

def can_handle(given_time):
    people = 0
    for t in times:
        people += (given_time // t)

    return people


MIN_GIVEN_TIME = 0
MAX_GIVEN_TIME = max(times)+1

l, r = MIN_GIVEN_TIME, MAX_GIVEN_TIME

while l < r:
    mid = (l+r)//2
    condition = NEED_TO_HANDLE <= can_handle(mid)
    if NEED_TO_HANDLE == can_handle(mid):
        ...