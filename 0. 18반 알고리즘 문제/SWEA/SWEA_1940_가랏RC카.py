"""
문제 정보
    https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PjMgaALgDFAUq
    *
작성
    양승현
    2023 02 04
"""

T = int(input())

for test_case in range(1, T + 1):
    N, distance, speed = int(input()), 0, 0
    for _ in range(N):
        op = input()

        if op != '0':
            way, acc = map(int, op.split())
            speed = speed + acc * (1 if way == 1 else -1)
            speed = max(speed, 0)

        distance = distance + speed

    print(f'#{test_case} {distance}')