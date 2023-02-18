from collections import deque

def solution(arg):
    map = [[x for x in row] for row in arg]
    ROW, COL = len(map), len(map[0])

    dist_to = {'L': float('inf'), 'E': float('inf')}

    def bfs(i, j, find):
        q = deque([(i, j)])
        visited = set()
        dist = 0
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                if map[i][j] == find:
                    dist_to[find] = min(dist_to[find], dist)
                    return
                for di, dj in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                    ni, nj = i + di, j + dj
                    if not (0 <= ni < ROW and 0 <= nj < COL): continue
                    if map[ni][nj] == 'X': continue
                    if (ni, nj) in visited: continue

                    visited.add((ni, nj))
                    q.append((ni, nj))
            dist += 1


    for i in range(ROW):
        for j in range(COL):
            if map[i][j] == 'S':
                bfs(i, j, 'L')
            if map[i][j] == 'L':
                bfs(i, j, 'E')

    d = dist_to['L'] + dist_to['E']
    return d if d < float('inf') else -1








args = [
    [["SOOOL", "XXXXO", "OOOOO", "OXXXX", "OOOOE"]],
    [["LOOXS", "OOOOX", "OOOOO", "OOOOO", "EOOOO"]]
]

sols = [
    16,
    -1
]

for a, s in zip(args, sols):
    res = solution(*a)
    if res != s:
        print(f'result {res} differ from {s}\n')

print('test finished')