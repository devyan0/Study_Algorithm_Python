"""
문제 정보
    https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWuSgKpqmooDFASy
    *

작성
    양승현
    2023 02 06
"""
import sys
sys.stdin = open("input.txt", "r")


from heapq import heappop as pop, heappush as push

T = int(input())

for test_case in range(1, T+1):
    N, D = map(int, input().split())
    conseq, acc = [], 0
    for x in input().split():
        if x == '0': acc += 1
        if x == '1':
            push(conseq, -acc)
            acc = 0

    push(conseq, -acc)

    cnt = 0
    while conseq and D <= -conseq[0]:
        largest = -pop(conseq)
        s1, s2 = largest//2, largest - largest//2 -1
        if s1 >= D: push(conseq, -s1)
        if s2 >= D: push(conseq, -s2)
        cnt += 1

    print(f'#{test_case} {cnt}')

