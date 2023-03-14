import sys
sys.stdin = open('input.txt', 'r')

"""
Backtracking with memoization
Time Complexity: O(K!NM) < 6!*50*50 < 6 Million -> feasible
    K: number of keys
    N: number of rows
    M: number of columns

Initially failed due to recursion limit 
"""

import sys
sys.setrecursionlimit(int(1e9))

from collections import defaultdict

N, M = map(int, input().split())
maze = [list(input()) for _ in range(N)]

# visited = defaultdict(lambda: defaultdict(set))
visited = [[set() for _ in range(M)] for _ in range(M)]
res = float('inf')

def bt(i, j, keys, hop):
    global res

    # branch
    if res <= hop: return

    # base case: out of range, wall
    if not (0 <= i < N and 0 <= j < M) or maze[i][j] == '#': return

    # base case: found exit
    cur = maze[i][j]
    if cur == '1':
        res = min(res, hop)
        return

    # base case: no keys in hand
    if cur in 'ABCDEF':
        s = ord(cur)-ord('A')
        if not (keys & (1 << s)): return

    # add key if found
    if cur in 'abcdef':
        s = ord(cur)-ord('a')
        keys = keys | (1 << s)

    # base case: visited
    if keys in visited[i][j]: return
    visited[i][j].add(keys)

    # backtracking
    for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        ni, nj = i + di, j + dj
        bt(ni, nj, keys, hop+1)


for i in range(N):
    for j in range(M):
        if maze[i][j] == '0':
            bt(i, j, 0, 0)


print(res if res < float('inf') else -1)

