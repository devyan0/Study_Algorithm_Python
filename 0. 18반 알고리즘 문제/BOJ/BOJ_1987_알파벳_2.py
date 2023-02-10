"""
문제 정보
    https://www.acmicpc.net/problem/1987
    * Optimization trade off

작성
    양승현
    2023 02 10
"""
import sys
input = sys.stdin.readline

R, C = map(int, input().split())
board = [[x for x in input()] for _ in range(R)]
visited = [False for _ in range(26)]
res = 0

def bt(r, c, step):
    global res

    res = max(res, step)

    cur = ord(board[r][c]) - ord('A')
    if visited[cur]: return



    for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        nr, nc = r + dr, c + dc
        if not (0<=nr<R and 0<=nc<C): continue

        visited[cur] = True
        bt(nr, nc, step+1)
        visited[cur] = False


bt(0, 0, 0)

print(res)
