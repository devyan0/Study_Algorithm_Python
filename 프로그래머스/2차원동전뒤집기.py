from collections import deque
# TLE
def solution(beginning, target):
    ROW, COL = len(beginning), len(beginning[0])

    q = deque([[[False] * ROW, [False] * COL, 0]])
    visited = set()

    def check(flip_row, flip_col):
        for i in range(ROW):
            for j in range(COL):
                if beginning[i][j] ^ flip_row[i] ^ flip_col[j] != target[i][j]:
                    return False
        return True

    while q:
        fr, fc, cost = q.popleft()
        if check(fr, fc):
            return cost

        if tuple(fr+fc) in visited:
            continue
        visited.add(tuple(fr+fc))

        for i in range(ROW):
            new_fr = fr[::]
            new_fr[i] ^= True
            q.append([new_fr, fc, cost+1])

        for j in range(COL):
            new_fc = fc[::]
            new_fc[j] ^= True
            q.append([fr, new_fc, cost+1])

    return -1


args = [
    [[[0, 1, 0, 0, 0], [1, 0, 1, 0, 1], [0, 1, 1, 1, 0], [1, 0, 1, 1, 0], [0, 1, 0, 1, 0]], [[0, 0, 0, 1, 1], [0, 0, 0, 0, 1], [0, 0, 1, 0, 1], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]],
    [[[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[1, 0, 1], [0, 0, 0], [0, 0, 0]]],

]

sols = [
    5,
    -1
]

for a, s in zip(args, sols):
    res = solution(*a)
    if res != s:
        print(f'result {res} differ from {s}')

print('test finished')