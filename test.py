from collections import defaultdict

class Node:
    def __init__(self, vt, i, j):
        self.i, self.j = i, j
        self.val = "EMPTY"
        self.vt = vt

    def set_value(self, val):
        if self.val != "EMPTY":
            self.vt[self.val].remove(self)
        self.vt[val].add(self)
        self.val = val


def solution(commands):
    vt = defaultdict(set)
    uf = {}
    table = [[Node(vt, i, j) for j in range(51)] for i in range(51)]
    res = []

    # returns the root
    def find(n):
        nonlocal uf
        if n not in uf:
            uf[n] = n

        if n != uf[n]:
            uf[n] = find(uf[n])

        return uf[n]

    for cmd in commands:
        info = cmd.split(' ')
        if info[0] == 'UPDATE' and len(info) == 4:
            r, c, val = info[1:]
            r, c = int(r), int(c)
            node = table[r][c]
            root = find(node)
            for i in range(51):
                for j in range(51):
                    if find(table[i][j]) == root:
                        table[i][j].set_value(val)

        if info[0] == 'UPDATE' and len(info) == 3:
            val1, val2 = info[1:]
            for n in vt[val1].copy():
                n.set_value(val2)
            # vt[val2] |= vt[val1]
            # vt[val1] = set()

        if info[0] == 'MERGE':
            r1, c1, r2, c2 = map(int, info[1:])
            n1, n2 = table[r1][c1], table[r2][c2]
            if n1 == n2: continue
            root1, root2 = find(n1), find(n2)
            uf[root2] = root1

            val = root1.val if root1.val != 'EMPTY' else root2.val
            for chk in uf:
                if uf[chk] == root1:
                    chk.set_value(val)


        if info[0] == 'UNMERGE':
            r, c = map(int, info[1:])
            root = uf[table[r][c]]
            val = root.val
            for i in range(51):
                for j in range(51):
                    n = table[i][j]
                    if n in uf and uf[n] == root:
                        n.val = "EMPTY"
                        del uf[n]
            table[r][c].set_value(val)


        if info[0] == 'PRINT':
            r, c = map(int, info[1:])
            res.append(table[r][c].val)

    print(res)
    return res



args1 = ["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]
sol1 = ["EMPTY", "group"]

args2 = ["UPDATE 1 1 a", "UPDATE 1 2 b", "UPDATE 2 1 c", "UPDATE 2 2 d", "MERGE 1 1 1 2", "MERGE 2 2 2 1", "MERGE 2 1 1 1", "PRINT 1 1", "UNMERGE 2 2", "PRINT 1 1"]
sol2 = ["d", "EMPTY"]

# res1 = solution(args1)
# print("#1 test passed" if sol1 == res1 else "fail")

res2 = solution(args1)
print("#2 test passed" if sol2 == res2 else "fail")
