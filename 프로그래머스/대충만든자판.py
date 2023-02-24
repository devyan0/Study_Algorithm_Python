from collections import defaultdict

def solution(keymap, targets):
    d = defaultdict(lambda: float('inf'))
    for km in keymap:
        for i, c in enumerate(km):
            d[c] = min(d[c], i+1)

    res = []
    for t in targets:
        cnt = 0
        for k in t:
            if d[k] == float('inf'):
                cnt = -1
                break
            cnt += d[k]
        res.append(cnt)

    return res



args = [
    [["ABACD", "BCEFD"], ["ABCD", "AABB"]],
    [["AA"], ["B"]],
    [["AGZ", "BSSS"], ["ASA", "BGZ"]],
]

sols = [
    [9, 4],
    [-1],
    [4, 6],
]

for a, s in zip(args, sols):
    res = solution(*a)
    if res != s:
        print(f'result {res} differ from {s}')

print('test finished')