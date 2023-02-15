"""
https://www.acmicpc.net/problem/1781

익숙하지 않은 유형
정합성 판단이 잘 안 서서 정렬로 풀려고 했는데 모순
"""
from heapq import heappush as push, heappop as pop
import sys
input = sys.stdin.readline

N = int(input())
info = sorted([list(map(int, input().split())) for _ in range(N)])

res, save, t = 0, 1, info[-1][0]
tasks = []
while 0 < t:
    while info and t <= info[-1][0]:
        push(tasks, -info.pop()[1])

    if 0 < save and tasks:
        res += -pop(tasks)
        save -= 1

    t, save = t-1, save+1

print(res)

"""

3
3 5
3 4
1 1
=> 10


9
5 5
4 6
4 12
3 8
4 18
2 10
2 5
1 7
1 14



와 같은 경우, 위와 같이 해결하면

1일 14개, 2일 10개, 3일 8개, 4일 12개, 5일 5개를 받으나

1일날 14개 (1일데드라인)
2일날 10개 (2일데드라인)
3일날 18개 (4일데드라인)
4일날 12개 (4일데드라인)
5일날 5개 (5일데드라인)

이 최선의 경우입니다.
"""