"""
fail
"""
import sys
sys.stdin = open('2_input_sample.txt', 'r')

from heapq import heappush as push, heappop as pop

def get_50(n, depth, MAX=50):
    base = 10**depth
    if divmod(n, 10**depth)[0] < 10:
        return list(range(base, min(n, base+MAX)))
    else:
        return [base] + get_50(n, depth+1) + list(range(base+1, min(n, base+9)))

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    print(f'#{tc}', end=' ')
    for fn in get_50(N+1, 0):
        print(f'{fn}.png', end=' ')
    print()

