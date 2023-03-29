import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
tree = [None] * (N+1)

for level in range(1, N+1):
    tree[level] = list(map(int, input().split()))   # number of the node, left, right


def bfs():
    ...

