"""
문제 정보
    https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14hwZqABsCFAYD
    *
작성
    양승현
    2023 02 04
"""

import sys
sys.stdin = open("input.txt", "r")

def get_dec(seq):
    if not seq: return 0
    prev, cnt = seq[0], 0
    for n in seq:
        if prev < n: cnt += 1
        prev = n

    return cnt


for test_case in range(1, 11):
    _ = input()
    cols = [[] for _ in range(100)]

    for i in range(100):
        row = list(map(int, input().split()))
        for j, n in enumerate(row):
            if not n: continue
            cols[j].append(n)

    print(f'#{test_case} {sum([get_dec(col) for col in cols])}')

