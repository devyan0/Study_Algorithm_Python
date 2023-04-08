import sys
sys.stdin = open('input.txt', 'r')

from collections import defaultdict

def main():
    n, m = map(int, input().split())
    p = defaultdict(list)
    input()  # Ignore the first input, as it's always 1 and not needed for this problem
    for _ in range(2, n + 1):
        x = int(input())
        p[x].append(_)

    lazy = [0] * (4 * n + 1)
    tree = [0] * (4 * n + 1)
    l = [0] * (n + 1)
    r = [0] * (n + 1)

    # Depth-first search to populate l and r lists
    def dfs(now, o):
        o[0] += 1
        l[now] = o[0]
        for next_node in p[now]:
            dfs(next_node, o)
        r[now] = o[0]

    o = [0]
    dfs(1, o)

    # Update lazy values in the tree
    def update_lazy(node, s, e):
        if lazy[node]:
            tree[node] += (e - s + 1) * lazy[node]
            if s != e:
                lazy[node * 2] += lazy[node]
                lazy[node * 2 + 1] += lazy[node]
            lazy[node] = 0

    # Update the segment tree values
    def update(node, s, e, i, j, v):
        update_lazy(node, s, e)
        if j < s or e < i:
            return
        if i <= s and e <= j:
            tree[node] += (e - s + 1) * v
            if s != e:
                lazy[node * 2] += v
                lazy[node * 2 + 1] += v
            return
        m = (s + e) // 2
        update(node * 2, s, m, i, j, v)
        update(node * 2 + 1, m + 1, e, i, j, v)
        tree[node] = tree[node * 2] + tree[node * 2 + 1]

    # Query the segment tree
    def query(node, s, e, idx):
        update_lazy(node, s, e)
        if idx < s or e < idx:
            return 0
        if s == e:
            return tree[node]
        m = (s + e) // 2
        return query(node * 2, s, m, idx) + query(node * 2 + 1, m + 1, e, idx)

    for _ in range(m):
        c, *args = map(int, input().split())
        if c == 1:
            x, y = args
            update(1, 1, n, l[x], r[x], y)
        elif c == 2:
            x = args[0]
            print(query(1, 1, n, l[x]))

if __name__ == "__main__":
    main()
