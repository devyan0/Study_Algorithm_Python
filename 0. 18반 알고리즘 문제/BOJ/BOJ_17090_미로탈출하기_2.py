import sys
sys.stdin = open('input.txt', 'r')
"""
Optimization never works for O(n^3) for python ...
use graph construction of O(n^2) which might work
"""
MOVE = {'U': (-1, 0), 'R': (0, 1), 'D': (1, 0), 'L': (0, -1)}

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

out_of_bound = lambda i, j: not (0 <= i < N) or not (0 <= j < M)
check = set([(i, j) for i in range(N) for j in range(M)])

for k in range(N+M):
    escaped = set()
    for i, j in check:
        if (i, j) not in check: continue
        di, dj = MOVE[board[i][j]]
        ni, nj = i+di, j+dj

        if out_of_bound(ni, nj) or (ni, nj) not in check:
            escaped.add((i, j))

    check ^= escaped


print(N*M - len(check))

