from collections import deque

def solution(map):
    q = deque([(0, 0, 0, 0)])   # x, y, dir, cnt
    N = len(map)
    visited = set()
    while q:
        i, j, dir, cnt = q.popleft()
        if (i, j, dir) in visited: continue
        visited.add((i, j, dir))

        if (i, j, dir) == (N-1, N-2, 0) or (i, j, dir) == (N-2, N-1, 1):
            return cnt

        if dir == 0:
            # linear move
            if j+2 < N and map[i][j+2] == 0:
                q.append((i, j+1, 0, cnt+1))
            if 0 <= j-1 and map[i][j-1] == 0:
                q.append((i, j-1, 0, cnt+1))
            if i+1 < N and map[i+1][j] == 0 and map[i+1][j+1] == 0:
                q.append((i+1, j, 0, cnt+1))
            if 0 <= i-1 and map[i-1][j] == 0 and map[i-1][j+1] == 0:
                q.append((i-1, j, 0, cnt+1))

            # rotate
            if i+1 < N:
                if map[i+1][j] == 0:
                    q.append((i, j, 1, cnt+1))
                if map[i+1][j+1] == 0:
                    q.append((i, j+1, 1, cnt+1))
            if 0 <= i-1:
                if map[i-1][j] == 0:
                    q.append((i-1, j, 1, cnt+1))
                if map[i-1][j+1] == 0:
                    q.append((i-1, j+1, 1, cnt+1))

        if dir == 1:
            # linear move
            if i+2 < N and map[i+2][j] == 0:
                q.append((i+1, j, 1, cnt+1))
            if 0 <= i-1 and map[i-1][j] == 0:
                q.append((i-1, j, 1, cnt+1))
            if j+1 < N and map[i][j+1] == 0 and map[i+1][j+1] == 0:
                q.append((i, j+1, 1, cnt+1))
            if 0 <= j-1 and map[i][j-1] == 0 and map[i+1][j-1] == 0:
                q.append((i, j-1, 1, cnt+1))

            # rotate
            if 0 <= j-1:
                if map[i][j-1] == 0:
                    q.append((i, j-1, 0, cnt+1))
                if map[i+1][j-1] == 0:
                    q.append((i+1, j-1, 0, cnt+1))
            if j+1 < N:
                if map[i][j+1] == 0:
                    q.append((i, j, 0, cnt+1))
                if map[i+1][j+1] == 0:
                    q.append((i+1, j, 0, cnt+1))


args = [
    [[[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]]
]

sols = [
    7
]

for a, s in zip(args, sols):
    res = solution(*a)
    if res != s:
        print(f'result {res} differ from {s}')

print('test finished')