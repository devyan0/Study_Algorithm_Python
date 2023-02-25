from collections import deque

class Node():
    def __init__(self, n):
        self.n = n
        self.child = []
        self.par = []

    def __str__(self):
        return f'{self.n}'

def solution(n, results):
    players = [Node(i) for i in range(n+1)]

    for w, l in results:
        winner, loser = players[w], players[l]
        winner.child.append(loser)
        loser.par.append(winner)

    def down(node, vis):
        if node in vis:
            return 0
        vis.add(node)
        acc = 1
        for c in node.child:
            acc += down(c, vis)

        return acc

    def up(node, vis):
        if node in vis: return 0
        vis.add(node)
        acc = 1
        for p in node.par:
            acc += up(p, vis)
        return acc

    res = 0
    for p in players:
        w, l = down(p, set()), up(p, set())
        if w + l == n + 1: res += 1

    return res


args = [
    [5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]],
]

sols = [
    2,
]

for a, s in zip(args, sols):
    res = solution(*a)
    if res != s:
        print(f'result {res} differ from {s}')

print('test finished')