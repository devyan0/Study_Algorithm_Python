import sys
sys.stdin = open('sample_input.txt', 'r')
input = sys.stdin.readline

class Node:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
        self.cnt = 1

    def insert(self, val):
        self.cnt += 1
        if val < self.val:
            if self.left:
                self.left.insert(val)
            else:
                self.left = Node(val)
        if self.val <= val:
            if self.right:
                self.right.insert(val)
            else:
                self.right = Node(val)

    def _rebalance(self):
        lc = self.left.cnt if self.left else 0
        rc = self.right.cnt if self.right else 0

        if lc < rc:
            ...
        elif rc < lc:
            l = self.left



T = int(input())
for tc in range(1, T+1):
    N, A = map(int, input().split())
    root = Node(A)




