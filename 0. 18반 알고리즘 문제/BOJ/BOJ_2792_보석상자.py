"""
문제 정보
    https://www.acmicpc.net/problem/2792
    *

작성
    양승현
    2023 02 09
"""
from math import ceil
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
colors = [int(input()) for _ in range(M)]

# required people to make max value as bound
need_person = lambda bound: sum([ceil(c/bound) for c in colors])

l, r = 1, max(colors)+1
while l < r:
    mid = (l+r) // 2
    np = need_person(mid)

    if np <= N:
        r = mid
    else:
        l = mid + 1

print(l)



