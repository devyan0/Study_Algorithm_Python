import sys
sys.stdin = open("input.txt", "r")

class Node:
    def __init__(self):
        self.val = '?'
        self.parent = None
        self.left = None
        self.right = None

def in_order(root, tree):
    if not root: return

    if root.left:
        in_order(tree[root.left], tree)
    print(root.val, end='')
    if root.right:
        in_order(tree[root.right], tree)


for tc in range(1, 11):
    N = int(input())
    nodes = [Node() for i in range(N+1)]

    for _ in range(N):
        info = input().split()
        idx = int(info[0])
        nodes[idx].val = info[1]

        if len(info) == 4:
            c1, c2 = map(int, info[2:])
            nodes[idx].left = c1
            nodes[idx].right = c2

        if len(info) == 3:
            c1 = int(info[2])
            nodes[idx].left = c1

    print(f'#{tc} ', end='')
    in_order(nodes[1], nodes)
    print()