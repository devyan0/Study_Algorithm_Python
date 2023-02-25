from collections import defaultdict

def solution(s):
    index_sum = defaultdict(int)
    cnt = defaultdict(int)
    result = 0

    acc_prev = defaultdict(lambda: [0] * len(s))
    for ci in range(ord('a'), ord('z')+1):
        c = chr(ci)
        acc = 0
        temp_cnt = 0
        for i, sc in enumerate(s):
            if sc != c:
                acc += temp_cnt*i
                temp_cnt = 0
            else:
                temp_cnt += 1
            acc_prev[c][i] = acc

    # for k in acc_prev:
    #     print(k, acc_prev[k])

    for i, c in enumerate(s):
        add = int(i*(i+1)/2)
        sub = i * cnt[c] - index_sum[c]
        if 0 < i: add += i * cnt[c]-acc_prev[c][i-1]
        cnt[c]+=1
        index_sum[c]+=i
        result += add - sub
        print(f'add: {add}, sub: {sub}, result: {result}')
    print()
    return result

args = [
    ["baby"],
    ["oo"],
]

sols = [
    9,
    0,
]

for a, s in zip(args, sols):
    res = solution(*a)
    if res != s:
        print(f'result {res} differ from {s}')

print('test finished')