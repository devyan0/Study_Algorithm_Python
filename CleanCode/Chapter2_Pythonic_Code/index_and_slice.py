# 파이썬이 다른 언어보다 편리한 점

# 1. 리스트의 마지막 요소 접근
nums = [1, 3, 5, 7, 9]
N = len(nums)
print(nums[-1])     # 마지막 원소인 9 접근

for i in range(1, N+1):
    print(nums[-i], end=' ')
print()

# 뒤에서 n번째는 앞에서 0번째와 같다
print(nums[-N])     # nums[0]와 같음

# print(nums[N])      # IndexError: list index out of range
# print(nums[-N-1])   # IndexError: list index out of range

# copy list
copied1 = nums
copied2 = nums[:]
copied3 = nums[::]

print(id(copied1) == id(nums))
print(id(copied2) == id(nums))
print(id(copied3) == id(nums))

# steps
jumps = nums[::2]
print(jumps)

# same thing using slice built-in
# 사용하지 않은 변수는 None으로 지정
interval = slice(None, 3)
print(nums[interval] == nums[:3])

# __getitem__

# __getitem__, __len__ 만 구현 돼 있으면 될까 -> yes

class mySeq:
    def __init__(self, nums):
        self.nums = nums

    def __getitem__(self, item):
        return item

    def __len__(self):
        return len(self.nums)

ms = mySeq(nums)
print(ms.nums)
print(ms["je;;":234234:'kkk'])


print('named tuple compare start')
real_slice = slice('aaa', 123, 'ddd')
from collections import namedtuple

TupleSlice = namedtuple("TupleTypeSlice", ['start', 'end', 'step'])
tuple_slice = TupleSlice('aaa', 123, 'ddd')
print(real_slice)
print(tuple_slice)
print(real_slice.start, tuple_slice.start)
print('named tuple compare ends')
"""
see 
https://docs.python.org/3/library/collections.html#collections.namedtuple
https://docs.python.org/3/library/functions.html#slice
"""

# range의 index는 range
"""
https://docs.python.org/3/library/functions.html#func-range
https://docs.python.org/3/library/stdtypes.html#typesseq
"""

def test(*args, **kwargs):
    print(args)
    print(kwargs)

test(*tuple_slice)  # not the dict type
td = {'a': 'aaa', 'b': 777}
test(*td)   # also just keys