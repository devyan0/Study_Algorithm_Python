"""
문제 정보
    https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWIsY84KEPMDFAWN
    *
작성
    양승현
    2023 02 05
"""
import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    cards = input()
    counts = {'S': {}, 'D': {}, 'H': {}, 'C': {}}
    error = False
    for i in range(0, len(cards), 3):
        kind, num = cards[i], cards[i+1:i+3]
        if counts[kind].setdefault(num, 0): error = True
        counts[kind][num] += 1

    if error: print(f'#{test_case} ERROR')
    else:
        print(f'#{test_case}', end=' ')
        for key in counts:
            print(13-sum(counts[key].values()), end=' ')
        print()
