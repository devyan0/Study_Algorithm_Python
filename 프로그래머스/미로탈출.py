from copy import deepcopy

def solution(arg):
    map = [[x for x in row] for row in arg]
    ROW, COL = len(map), len(map[0])

    dist_to = {'L': float('inf'), 'E': float('inf')}

    def dfs(i, j, temp, find):
        if map[i][j] == find:
            dist_to[find] = min(temp, dist_to[find])
            return

        for di, dj in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            ni, nj = i+di, j+dj
            if not (0 <= ni < ROW and 0 <= nj < COL): continue
            if map[ni][nj] == 'X':
                continue

            map[i][j] = 'X'
            dfs(ni, nj, temp+1, find)
            map[i][j] = 'O' # watch out its not prev one

    for i in range(ROW):
        for j in range(COL):
            if map[i][j] == 'S':
                temp = deepcopy(map)
                dfs(i, j, 0, 'L')
                map = temp
            if map[i][j] == 'L':
                temp = deepcopy(map)
                dfs(i, j, 0, 'E')
                map = temp

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