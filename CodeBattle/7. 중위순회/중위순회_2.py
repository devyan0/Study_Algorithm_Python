import sys
sys.stdin = open('input.txt', 'r')

"""
완전 이진트리라는 조건이 있으면 1차원 배열을 사용하는 게 좋다
구현이 간단해진다
"""

def dfs(arr, n, N):
    if N < n: return
    dfs(arr, 2*n, N)
    print(arr[n], end='')
    dfs(arr, 2*n+1, N)

for tc in range(1, 11):
    N = int(input())
    arr = [''] + [input().split()[1] for _ in range(N)]

    print(f'#{tc} ')
    dfs(arr, 1, N)
    print()

