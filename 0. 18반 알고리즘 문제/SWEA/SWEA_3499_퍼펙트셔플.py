"""
문제 정보
    https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWGsRbk6AQIDFAVW
    *
작성
    양승현
    2023 02 05
"""
import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    cards = input().split()
    res = []
    center = N//2
    if N%2: center += 1
    for i in range(center):
        res.append(cards[i])
        if i+center < N: # N % 2 == 1, last remove
            res.append(cards[i+center])

    print(f'#{test_case}', end=' ')
    for word in res:
        print(word, end=' ')
    print()
