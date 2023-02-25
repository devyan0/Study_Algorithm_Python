
def solution(commands):
    MAX = 51
    res = []
    merged = [[(i, j) for j in range(MAX)] for i in range(MAX)]
    values = [[None for _ in range(MAX)] for _ in range(MAX)]

    for c in commands:
        info = c.split(' ')
        if info[0] == 'UPDATE':
            if len(info) == 4:
                _, r, c, val = info
                x, y = merged[int(r)][int(c)]
                values[x][y] = val

            if len(info) == 3:
                _, old_val, new_val = info
                for i, row in enumerate(values):
                    for j, val in enumerate(row):
                        if val == old_val:
                            values[i][j] = new_val

        if info[0] == 'MERGE':
            _, r1, c1, r2, c2 = info
            r1, c1, r2, c2 = int(r1), int(c1), int(r2), int(c2)
            x1, y1 = merged[r1][c1]
            x2, y2 = merged[r2][c2]
            val1 = values[x1][y1]
            val2 = values[x2][y2]
            for i in range(MAX):
                for j in range(MAX):
                    if merged[i][j] == (x2, y2):
                        merged[i][j] = (x1, y1)
            if val1: values[x1][y1] = val1
            elif val2: values[x1][y1] = val2

        if info[0] == 'UNMERGE':
            _, r, c = info
            r, c = int(r), int(c)
            x, y = merged[r][c]
            val = values[x][y]
            for i in range(MAX):
                for j in range(MAX):
                    # if merged[i][j] == merged[x][y]: <- 원본이 훼손돼 중간에 로직이 망가진다
                    if merged[i][j] == (x, y):
                        merged[i][j] = (i, j)
                        values[i][j] = None
            values[r][c] = val

        if info[0] == 'PRINT':
            _, r, c = info
            r, c = int(r), int(c)
            x, y = merged[r][c]
            res.append(values[x][y] if values[x][y] else 'EMPTY')


    return res

args = [
    [	["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]],
    [	["UPDATE 1 1 a", "UPDATE 1 2 b", "UPDATE 2 1 c", "UPDATE 2 2 d", "MERGE 1 1 1 2", "MERGE 2 2 2 1", "MERGE 2 1 1 1", "PRINT 1 1", "UNMERGE 2 2", "PRINT 1 1"]],
]

sols = [
    ["EMPTY", "group"],
    ["d", "EMPTY"],
]

for a, s in zip(args, sols):
    res = solution(*a)
    if res != s:
        print(f'result {res} differ from {s}')

print('test finished')

"""
["UPDATE 1 1 A", "UPDATE 2 2 B", "UPDATE 3 3 C", "UPDATE 4 4 D", "MERGE 1 1 2 2", "MERGE 3 3 4 4", "MERGE 1 1 4 4", "UNMERGE 3 3", "PRINT 1 1", "PRINT 2 2", "PRINT 3 3", "PRINT 4 4"]
답은 ["EMPTY", "EMPTY", "A", "EMPTY"]가 나와야 합니다. ["A", "A", "EMPTY", "A"]나 ["EMPTY", "EMPTY", "A", "A"] 같은 이상한 답이 나오지 않는지 확인해 주세요.
"""