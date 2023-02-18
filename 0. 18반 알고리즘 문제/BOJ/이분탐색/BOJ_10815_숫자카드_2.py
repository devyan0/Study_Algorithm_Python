"""
https://www.acmicpc.net/problem/10815
pin point, while-else
"""
import sys
input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))
cards.sort()

M = int(input())
finds = map(int, input().split())
for find in finds:
    l, r = 0, len(cards)            # 열린 조건
    while l < r:                    # 열린 조건
        mid = (l+r) // 2
        check = cards[mid]
        if find == check:
            print(1, end=' ')
            break
        elif find < check:
            r = mid                 # 열린 조건
        elif check < find:
            l = mid + 1

    else:
        print(0, end=' ')

