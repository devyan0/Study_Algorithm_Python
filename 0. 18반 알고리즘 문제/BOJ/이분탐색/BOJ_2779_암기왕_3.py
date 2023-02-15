"""
문제 정보
    https://www.acmicpc.net/problem/2776
    *

작성
    양승현
    2023 02 14
"""

import sys
input = sys.stdin.readline

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    seen = list(map(int, input().split()))
    seen.sort()

    M = int(input())
    finds = map(int, input().split())
    for find in finds:
        l, r = 0, len(seen)
        while l < r:
            mid = (l+r)//2
            if find <= seen[mid]:
                r = mid
            else:
                l = mid + 1

        # l pointing to possible num
        if l < len(seen) and seen[l] == find: print(1)
        else: print(0)

