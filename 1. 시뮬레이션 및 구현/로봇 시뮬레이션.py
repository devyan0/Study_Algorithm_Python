"""
문제 정보
    로봇 시뮬레이션 (골드 5)
    https://www.acmicpc.net/problem/2174
    *
작성
    양승현
    2023 02 24
"""

import sys

sys.setrecursionlimit(int(1e9))
input = sys.stdin.readline

# row B col A
A, B = map(int, input().split())

# N robots, M operations
N, M = map(int, input().split())

d = {}
X, Y, DIR = 0, 1, 2

NESW = ['N', 'E', 'S', 'W']
MOVE = {'N': (0, 1), 'W': (-1, 0), 'S': (0, -1), 'E': (1, 0)}

def R(cur, cnt=1):
    idx = NESW.index(cur)
    return NESW[(idx+cnt) % 4]

def L(cur, cnt=1):
    idx = NESW.index(cur)
    return NESW[(idx-cnt) % 4]

def forward(num, repeat, x, y, dir):
    dx, dy = MOVE[dir]
    for i in range(1, repeat+1):
        nx, ny = x+dx*i, y+dy*i
        if not (0<nx<=A and 0<ny<=B):
            print(f'Robot {num} crashes into the wall')
            return False
        for other in d:
            if other == num: continue
            ox, oy, _ = d[other]
            if (nx, ny) == (ox, oy):
                print(f'Robot {num} crashes into robot {other}')
                return False
        d[num] = [nx, ny, dir]
    return True

def operate():
    res = True
    for _ in range(M):
        num, op, repeat = input().split()
        if not res: continue

        num, repeat = int(num), int(repeat)
        if op == 'R': d[num][DIR] = R(d[num][DIR], repeat)
        if op == 'L': d[num][DIR] = L(d[num][DIR], repeat)
        if op == 'F':
            if not forward(num, repeat, *d[num]):
                res = False

    return res

for num in range(1, N+1):
    x, y, dir = input().split()
    d[num] = [int(x), int(y), dir]



if operate():
    print('OK')


