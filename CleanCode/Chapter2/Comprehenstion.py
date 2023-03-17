"""
컴프리헨션과 할당 표현식
1. 간결한 코드 작성 -> 가독성 향상
매우 주의 더 간결한 코드가 항상 더 나은 코드를 의미하는 것은 아니다
Keep it simple

가독성이 향상되는 지 확인
"""

# 원소가 제곱인 배열
nums = [1, 2, 3, 4]


square1 = []
for n in nums:
    square1.append(n**2)
print(f'square1: {square1}')

# 중복되는 append 연산을 한 줄로 표현
square2 = [n**2 for n in nums]
print(f'square2: {square2}')


def get_square_iter(nums):
    square = []
    for n in nums:
        square.append(n**2)
    return square

def get_square_comp(nums):
    return [n**2 for n in nums]

from dis import dis
# print('get_square_iter')
# dis(get_square_iter)
# print('get_square_comp')
# dis(get_square_comp)

"""
가독성이 실제로 향상 되는가?
nums 배열과 remove 집합(set)이 주어질 때, nums 배열에서 remove 집합에 포함되지 않은 
원소만만을 포함하는 배열을 반환하는 함수를 작성하라
"""
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
remove = {3, 6, 9}

result1 = []
for n in nums:
    if n in remove:
        continue
    result1.append(n)

print(f'result: {result1}')

result2 = [n for n in nums if n not in remove]
print(f'result: {result2}')

def arg_test(arg):
    print(f'arg={arg}')

arg_test(n for n in range(10) if n % 2 == 0)

print('================')
def expan_test():
    return *(x for x in range(10)),
dis(expan_test)