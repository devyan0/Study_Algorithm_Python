"""
문제 정보
    https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWVWgkP6sQ0DFAUO
    *

작성
    양승현
    2023 02 06
"""
import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    words = []
    for _ in range(5):
        w = [x for x in input()]
        words.append(w + [None] * (15-len(w)))

    res = ''
    for col in range(15):
        for row in range(5):
            if not words[row][col]: continue
            res += words[row][col]

    print(f'#{test_case} {res}')