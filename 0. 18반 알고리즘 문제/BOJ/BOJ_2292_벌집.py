"""
문제 정보
    https://www.acmicpc.net/problem/2292
    *

작성
    양승현
    2023 02 07
"""

import sys
input = sys.stdin.readline


N = int(input())

step = 1
cur = 1

while cur < N:
    cur += (6 * step)
    step += 1

print(step)
"""
1
7  +6
19 +12
37 +18
61 +24 
"""