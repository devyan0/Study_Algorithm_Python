"""
14 힙 직접 구현하고 자식 노드도 우선순위를 갖도록 heap 구현
그러면 중간 값을 heap[len(heqp)//2]으로 접근 가능
"""

from heapq import heappush as push, heappop as pop
import sys
sys.stdin = open('sample_input.txt', 'r')

class Tree:
    def __init__(self, mid):
        self.mid = mid
        self.left = []
        self.right = []

    def insert(self, n1, n2):
        n1, n2 = min(n1, n2), max(n1, n2)

        if self.mid < n1:
            push(self.left, -self.mid)
            push(self.right, n1)
            push(self.right, n2)
            self.mid = pop(self.right)
        elif n2 < self.mid:
            push(self.right, self.mid)
            push(self.left, -n1)
            push(self.left, -n2)
            self.mid = -pop(self.left)
        else:
            push(self.left, -n1)
            push(self.right, n2)

T = int(input())
for tc in range(1, T+1):
    N, A = map(int, input().split())
    res, MOD = 0, 20171109
    tree = Tree(A)
    for _ in range(N):
        n1, n2 = map(int, input().split())
        tree.insert(n1, n2)
        res += tree.mid % MOD

    print(f'#{tc} {res}')


