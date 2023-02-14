"""
only imp push and pop which is min heapq
"""

import sys
sys.stdin = open('sample_input.txt', 'r')

def _siftup(heap, idx):
    p = (idx-1) // 2
    while 0 < idx and heap[idx] < heap[p]:
        heap[idx], heap[p] = heap[p], heap[idx] # swap
        idx = p
        p = (idx-1) // 2

def _siftdown(heap, idx):
    child = 2*idx+1
    size = len(heap)
    while child < size:
        if child+1 < size and heap[child+1] < heap[child]:
            child += 1

        if heap[child] < heap[idx]:
            heap[child], heap[idx] = heap[idx], heap[child]
            idx = child
            child = 2*idx+1
        else:
            break


def push(heap, n):
    heap.append(n)
    _siftup(heap, len(heap)-1)

def pop(heap):
    last = heap.pop()
    if not heap: return last

    root = heap[0]
    heap[0] = last
    _siftdown(heap, 0)
    return root


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    q = []
    out = f'#{tc} '

    for n in range(N):
        in_ = input().split()
        if in_[0] == '1':
            push(q, -int(in_[1]))
        else:
            if q:
                out += f'{-pop(q)} '
            else:
                out += '-1 '

    print(out)

