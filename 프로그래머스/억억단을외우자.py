from math import isqrt
from collections import defaultdict
from bisect import bisect_left as bisect

def solution(e, starts):

    def count(n):
        res = 1
        if n == 1: return res

        for i in range(1, isqrt(n)+1):
            m, r = divmod(n, i)
            if r == 0:
                if m == n // m: res += 1
                else: res += 2
        return res

    d = defaultdict(list)

    for i in range(1, 10):
        print(i, count(i))

    for i in range(1, e+1):
        cnt = count(i)
        d[cnt].append(i)

    keyset = sorted(d.keys(), reverse=True)
    res = []
    for s in starts:
        for k in keyset:
            idx = bisect(d[k], s)
            if idx == len(d[k]): continue
            res.append(d[k][idx])
            break


    return res


args = [
    [8, [1, 3, 7]],
    [8, [3, 7]],
]

sols = [
    [6, 6, 8],
    [6, 8]
]

for a, s in zip(args, sols):
    res = solution(*a)
    if res != s:
        print(f'result {res} differ from {s}')

print('test finished')