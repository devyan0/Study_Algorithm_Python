"""
https://www.acmicpc.net/problem/2110
공유기 사이 거리 최대 = 공유기를 최소한으로 사용해서
조건 파악 : x_i 크니까 mid 탐색하는 범위는 집 거리
최소 거리의 최대화 -> 최소 거리를 범위 탐색

need        5 4 3 2 1
C           3 3 3 3 3
c <= need   T T T F F
                  l
                  return l - 1 ( = r - 1)

"""
import sys
input = sys.stdin.readline

N, WIFI_ON_HAND = map(int, input().split())
loc = sorted([int(input()) for _ in range(N)])
diff = [loc[i] - loc[i-1] for i in range(1, N)]

def wifi_needed(min_dist):
    acc = 0
    wifis = 1
    for d in diff:
        if d + acc < min_dist:
            acc += d
        else:
            wifis += 1
            acc = 0
    return wifis


l, r = 1, (max(loc)-min(loc)+1) // (WIFI_ON_HAND-1)
while l < r:
    mid = (l+r) // 2
    if WIFI_ON_HAND <= wifi_needed(mid):
        l = mid + 1
    else:
        r = mid

print(l-1)