"""
문제 정보
    https://www.acmicpc.net/problem/22866
    *

작성
    양승현
    2023 02 07
"""

import sys
input = sys.stdin.readline

# N = int(input())
# h = [int(x) for x in input().split()]
N = 8
h_list = [2, 1, 3, 1, 2, 4, 5, 4]
dp_r = [0 for _ in range(N)]
for i in range(2, N+1):
    j = i + 1
    while j < N and h_list[i] >= h_list[j]:
        j += 1
    if j < N:
        dp_r[i] = j


    h = heights[i]
    if h < h_prev:
        dp_r[i] = dp_r[i+1] + 1
    else:
        j = i + 1
        while j < N and h >= heights[j]:
            j += 1
        if j < N:
            dp_r[i] = dp_r[j]


    h_prev = i





