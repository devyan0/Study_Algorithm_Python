from heapq import heappush as push, heappop as pop, heapify
import sys
input = sys.stdin.readline

N = int(input())
info = [list(map(int, input().split()[1:][::-1])) for x in range(N)]
# [(end, start), ...]
heapify(info)
res, q = 0, []

for i in info:
    s, e = i
    if not q:
        push(q, i)
    else:
        if q[0][0] <= s:    # 가장 이른 종료 시간
            pop(q)
        push(q, i)

    res = max(res, len(q))

print(res)