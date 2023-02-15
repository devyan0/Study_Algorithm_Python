from collections import defaultdict
import sys
sys.setrecursionlimit(int(1e9))
input = sys.stdin.readline

N, M = map(int, input().split())
d = defaultdict(lambda: defaultdict(lambda: 0))

for _ in range(M):
    n1, n2, c = map(int, input().split())
    d[n1][n2] = max(d[n1][n2], c)
    d[n2][n1] = max(d[n2][n1], c)

def search(node, parent, w, target):
    if node == target:
        return True

    reach = False
    for child in d[node]:
        if child == parent: continue
        if reach: return reach
        cap = d[node][child]
        if w <= cap:
            reach = reach or search(child, node, w, target)

    return reach

s, e = map(int, input().split())
condition = lambda w: search(s, -1, w, e)

l, r = 1, 1_000_000_000 + 1
while l < r:
    mid = (l+r)//2
    if condition(mid):
        l = mid + 1
    else:
        r = mid

print(l-1)