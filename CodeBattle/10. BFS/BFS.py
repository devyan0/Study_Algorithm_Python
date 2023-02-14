import sys
sys.stdin = open('sample_input.txt', 'r')

class Node:
    def __init__(self, idx):
        self.idx = idx
        self.parent = None
        self.children = []

    def __str__(self):
        return str(self.idx)

from collections import deque

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nodes = [Node(i) for i in range(N+1)]

    for i, p in enumerate(map(int, input().split())):
        nodes[i+2].parent = nodes[p]
        nodes[p].children.append(nodes[i+2])

    # for i, n in enumerate(nodes):
    #     print(i, end=' ')
    #     if n.parent: print(n.parent.idx, end=' ')
    #     print([x.idx for x in n.children])

    q = deque([nodes[1]])
    move = 0
    depth = 0
    while q:
        for _ in range(len(q)):
            n = q.popleft()

            move += depth  # go to the node
            for ad in n.children:
                move += 1       # go pick
                if ad.children: q.append(ad)
                move += 1       # back to n

        # back to root
        move += depth

        # increase next depth
        depth += 1


    print(f'#{tc} {move-depth}')