
def solution(*arg):
    ...




args = [
    [["SOOOL", "XXXXO", "OOOOO", "OXXXX", "OOOOE"]],
    [["LOOXS", "OOOOX", "OOOOO", "OOOOO", "EOOOO"]],
]

sols = [
    16,
    -1,
]

for a, s in zip(args, sols):
    res = solution(*a)
    if res != s:
        print(f'result {res} differ from {s}')

print('test finished')