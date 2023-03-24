"""
falied

"""
import sys
sys.stdin = open('input.txt', 'r')

import sys
input = sys.stdin.readline
from collections import defaultdict

N, M = map(int, input().split())
graph = defaultdict(list)

for _ in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)

memo = {}
def cover_num(node, path):
    if node in memo: return memo[node]
    if node not in graph:
        return 1
    if node in path:
        return len(path)

    branch_len = [cover_num(child, path | {node}) for child in graph[node]]
    return 1 + max(branch_len) if branch_len else 1

res = {k: cover_num(k, set()) for k in graph}
print(*sorted([i for i in res if res[i] == max(res.values())]))
