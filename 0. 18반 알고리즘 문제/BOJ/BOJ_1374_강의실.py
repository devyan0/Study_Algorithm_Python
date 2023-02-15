from heapq import heappush as push, heappop as pop, heapify
import sys
input = sys.stdin.readline

N = int(input())
# info = [list(map(int, input().split()[1:][::-1])) for x in range(N)]
info = [list(map(int, input().split()[1:])) for x in range(N)]
# [(end, start), ...]
info.sort()
print(info)
res, q = 0, []

for i in info:
    print(f'{i} in')
    s, e = i
    if not q:
        push(q, e)
    else:
        if q[0] <= s:    # 가장 이른 종료 시간
            print(f'{q[0]} will pop')
            pop(q)
        push(q, e)
    print(f'now: {q}')
    print()

    res = max(res, len(q))

print(res)