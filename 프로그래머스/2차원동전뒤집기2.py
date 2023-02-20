from collections import deque

# bit manipulation -> halved time, but still TLE
def solution(beginning, target):
    ROW, COL = len(beginning), len(beginning[0])
    base = [''.join(str(x) for x in row) for row in beginning]
    base = [int(x, 2) for x in base]
    end = [''.join(str(x) for x in row) for row in target]
    end = [int(x, 2) for x in end]

    # q = deque([[(1<<ROW)-1, (1<<COL)-1, 0]])
    q = deque([[0, 0, 0]])
    visited = set()

    def check(flip_row, flip_col):
        for r in range(ROW):
            check = base[r]
            if 1<<r & flip_row != 0:
                check = check ^ ((1<<COL)-1)
            if check ^ end[r] ^ flip_col != 0: return False

        return True

    while q:
        fr, fc, cost = q.popleft()
        if check(fr, fc):
            return cost

        if (fr, fc) in visited:
            continue
        visited.add((fr, fc))

        for i in range(ROW):
            q.append([fr ^ (1<<i), fc, cost+1])

        for j in range(COL):
            q.append([fr, fc ^ (1<<j), cost+1])

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