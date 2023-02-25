
def solution(board):
    answer = -1
    return answer




args = [
    [	["O.X", ".O.", "..X"]],
    [	["OOO", "...", "XXX"]],
    [	["...", ".X.", "..."]],
    [	["...", "...", "..."]],
]

sols = [
    1,
    0,
    0,
    1
]

for a, s in zip(args, sols):
    res = solution(*a)
    if res != s:
        print(f'result {res} differ from {s}')

print('test finished')