import sys
sys.stdin = open('input.txt', 'r')


for tc in range(1, 11):
    _ = int(input())
    code = [int(x) for x in input().split()]
    M = int(input())
    for _ in range(M):
        print(input())

    print(f'#{tc} ')
