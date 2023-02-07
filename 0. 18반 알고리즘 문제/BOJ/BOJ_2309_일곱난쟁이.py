"""
문제 정보
    https://www.acmicpc.net/problem/2309
    *

작성
    양승현
    2023 02 07
"""

import sys
input = sys.stdin.readline


heights = []
res = []
for _ in range(9):
    heights.append(int(input()))
heights.sort()

def bt(i, path):
    global res

    if res: return

    if i == 9:
        if len(path) == 7 and sum(path) == 100:
            res = path
        return

    bt(i+1, path)
    bt(i+1, path+heights[i:i+1])

bt(0, [])

for i in res:
    print(i, end=' ')
