
def solution(n):
    # assert n % 2 == 0, "홀수면 터져라"
    l, r = 0, 100
    while l < r:
        l += 1
        r -= 1

    assert l != r, "뭔가 이상하다"


solution(1)