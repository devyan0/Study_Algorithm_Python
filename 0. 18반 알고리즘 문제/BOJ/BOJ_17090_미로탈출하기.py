import sys
sys.stdin = open('input.txt', 'r')
"""
TLE
"""
MOVE = {'U': (-1, 0), 'R': (0, 1), 'D': (1, 0), 'L': (0, -1)}

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
can_escape = [[False for _ in range(M)] for _ in range(N)]

out_of_bound = lambda i, j: not (0<=i<N) or not (0<=j<M)

for k in range(N+M):
    for i in range(N):
        for j in range(M):
            if can_escape[i][j]: continue

            di, dj = MOVE[board[i][j]]
            ni, nj = i+di, j+dj
            if out_of_bound(ni, nj):
                can_escape[i][j] = True
            elif can_escape[ni][nj]:
                can_escape[i][j] = True

print(sum([row.count(True) for row in can_escape]))

