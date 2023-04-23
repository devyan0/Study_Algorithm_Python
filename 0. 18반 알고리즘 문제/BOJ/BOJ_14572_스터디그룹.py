import sys
sys.stdin = open('input.txt', 'r')

N, K, D = map(int, input().split())
members = {}
for _ in range(N):
    M, d = map(int, input().split())
    algo = [list(map(int, input().split())) for _ in range(M)]