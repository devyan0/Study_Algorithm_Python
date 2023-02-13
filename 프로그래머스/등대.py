"""
https://school.programmers.co.kr/learn/courses/30/lessons/133500

"""

class Node:
    def __init__(self):
        self.children = []


def solution(n, lighthouse):
    nodes = [Node() for _ in range(n + 1)]
    for s, e in lighthouse:
        nodes[s].children.append(nodes[e])
        nodes[e].children.append(nodes[s])

    def dfs(node, parent, acc):
        # return root should on/off, acc on
        child_all_off = True
        child_all_on = True
        cnt = 0

        if node.children == [parent]:
            return False, 0

        for child in node.children:
            if child == parent: continue
            c_on, c_acc = dfs(child, node, acc)
            if c_on: child_all_off = False
            if not c_on: child_all_on = False
            cnt += c_acc

        if child_all_off:
            return True, cnt + 1
        if child_all_on:
            return False, cnt

        return True, cnt + 1
        # return can_off, cnt + (0 if can_off else 1)

    return dfs(nodes[1], nodes[0], 0)[1]

arg1 = [8, [[1, 2], [1, 3], [1, 4], [1, 5], [5, 6], [5, 7], [5, 8]]]
res1 = solution(*arg1)
print(f'res1: {res1}')

arg2 = [10, [[4, 1], [5, 1], [5, 6], [7, 6], [1, 2], [1, 3], [6, 8], [2, 9], [9, 10]]]
res2 = solution(*arg2)
print(f'res2: {res2}')

