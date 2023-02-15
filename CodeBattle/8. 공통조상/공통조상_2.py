from collections import defaultdict
import sys
sys.stdin = open("input.txt", "r")

def find(x, uf, res):
    if x not in uf:
        uf[x] = x

    if x != uf[x]:
        res.append(x)
        find(uf[x], uf, res)


def get_child_num(node, down):
    if not down[node]:
        return 1
    res = 0
    for c in down[node]:
        res += get_child_num(c, down)
    return res + 1

T = int(input())
for test_case in range(1, T+1):
    V, E, n1, n2 = map(int, input().split())
    up = defaultdict(lambda: None)
    down = defaultdict(lambda: [])
    info = [int(x) for x in input().split()]

    # split childs and parents
    for i in range(len(info)//2):
        parent, child = info[2*i], info[2*i+1]
        up[child] = parent
        down[parent].append(child)

    # prev=1 guarantees root common ancestor
    path1, path2, prev = [], [], 1
    find(n1, up, path1); find(n2, up, path2)

    for n1, n2 in zip(path1[::-1], path2[::-1]):
        if n1 == n2: prev = n1
        else: break

    # now, prev is the closest common ancestor
    childs_num = get_child_num(prev, down)
    print(f'#{test_case} {prev} {childs_num}')

