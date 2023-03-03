
def solution(n, m, section):
    answer = 0
    return answer




args = [
    [8, 4, [2, 3, 6]],
    [	5, 4, [1, 3]],
    [4, 1, [1, 2, 3, 4]],
]

sols = [
    2,
    1,
    4,
]

for a, s in zip(args, sols):
    res = solution(*a)
    if res != s:
        print(f'result {res} differ from {s}')

print('test finished')