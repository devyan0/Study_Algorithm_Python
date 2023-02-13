"""
[입력]
첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

각 테스트 케이스마다 첫째 줄에 수행해야하는 연산의 수를 나타내는 자연수 N(1≤N≤105)이 주어진다.

둘째 줄부터 N개의 줄에 걸쳐서 순서대로 수행해야하는 연산에 대한 정보가 주어진다.

연산 1을 수행해야 한다면 2개의 자연수 '1 x'가 주어지며, x(1≤x≤109)를 최대 힙에 추가하는 연산임을 의미한다.

연산 2를 수행해야 한다면 1개의 자연수 '2'가 주어지며, 현재 최대 힙의 루트 노드의 키값을 출력하고 해당 노드를 삭제하는 연산임을 의미한다.


[출력]
각 테스트 케이스마다 첫째 줄에 ‘#x’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고, 연산 2의 결과들을 공백 하나를 사이에 두고 순서대로 출력한다.

만약, 연산 2를 수행해야 하는데 힙에 원소가 없어서 출력해야 할 최대 키값이 존재하지 않는다면 -1을 출력한다.
"""
import sys
sys.stdin = open('sample_input.txt', 'r')

from heapq import heappush as push, heappop as pop

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

