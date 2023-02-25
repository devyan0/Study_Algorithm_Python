"""
Implementation of Binary Index Tree (aka. Fenwick Tree)
1. should consider the size of the tree
2. index manipulation
3. update vs manipulation (1-indexed)
"""

def bitify(arr):
    bit = [0 for _ in arr]
    for i, v in enumerate(arr):
        update(bit, i, v)

    return bit


def update(bit, idx, data):
    idx += 1
    while idx <= len(bit):
        bit[idx-1] += data
        idx += (idx & -idx)


def get(bit, idx):
    idx += 1
    res = 0
    while 0 < idx:
        res += bit[idx-1]
        idx &= idx - 1

    return res

arr = [5, 2, 3, 7, 2, -1, 4, 0]

print(f'arr: {arr}')

arr = bitify(arr)
print(f'bit: {arr}')

print(f'get idx = 2 to 5, sum={get(arr, 5)}-{get(arr, 1)}={get(arr, 5)-get(arr, 1)}')




