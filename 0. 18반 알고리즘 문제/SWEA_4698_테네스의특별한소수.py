"""
문제 정보
    https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWRuoqCKkE0DFAXt&
    * split steps
        - make prime table
        - check valid number
      checking prime can be optimized 
작성
    양승현
    2023 02 06
"""
import time
import sys
sys.stdin = open("sample_input.txt", "r")
start = time.time()

from math import sqrt
T = int(input())

def prime_check(start, end, special):
    prime_table = [True] * (end+1)
    prime_table[0], prime_table[1] = False, False
    special_cnt = 0

    for i in range(2, int(sqrt(end+1))+1):
        if not prime_table[i]: continue
        for j in range(i*i, end+1, i):
            prime_table[j] = False

    for i in range(2, end+1):
        if start <= i and prime_table[i] and special in str(i):
            special_cnt += 1

    return special_cnt



for test_case in range(1, T + 1):
    D, A, B = map(int, input().split())
    cnt = prime_check(A, B, str(D))

    print(f'#{test_case} {cnt}')


print()
print(f'took: {(time.time()-start)*1000:.0f} ms')
print(f'req: {4/100*1000:.0f} ms')

