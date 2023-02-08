T = int(input())

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

for test_case in range(1, T + 1):
    N = int(input())

    grid = [[0 for _ in range(N)] for _ in range(N)]
    i, j, val, head = 0, 0, 1, 0

    for _ in range(N ** 2):
        grid[i][j] = val
        val += 1

        di, dj = DIRS[head % 4]
        ni, nj = i + di, j + dj
        if not (0 <= ni < N and 0 <= nj < N) or grid[ni][nj]:
            head += 1
            di, dj = DIRS[head % 4]
            ni, nj = i + di, j + dj

        i, j = ni, nj

    print(f'#{test_case}')
    for row in grid:
        for e in row:
            print(e, end=' ')
        print()