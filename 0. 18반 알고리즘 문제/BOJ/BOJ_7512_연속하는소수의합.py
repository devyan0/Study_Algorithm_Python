import sys
sys.stdin = open('input.txt', 'r')

# 소수 리스트 만들기
def mk_prime_list(n):
    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n**0.5)+1):
        if is_prime[i]:
            for j in range(i*2, n, i):
                is_prime[j] = False

    return [i for i in range(n) if is_prime[i]]

primes = mk_prime_list(10_000)

def mk_prime_sum_list(window_size):
    ...






T = int(input())

for tc in range(1, T+1):
    _ = int(input())
    nums = list(map(int, input().split()))
