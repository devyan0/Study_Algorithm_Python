"""
컴프리헨션과 할당 표현식

"""
# 원본 리스트
nums = [1, 2, 3, 4, 5]

# 각 원소를 그대로 가져오는 리스트
nums_copy = [n for n in nums]               # [1, 2, 3, 4, 5]

# 각 원소를 제곱한 리스트
square_nums = [n**2 for n in nums]          # [1, 4, 9, 16, 25]

# 각 원소의 짝수만 가져온 리스트
even_nums = [n for n in nums if n % 2 == 0] # [2, 4]


# [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
idx_num_pair = [(idx, n) for idx, n in enumerate(nums)]

print(nums_copy)
print(square_nums)
print(even_nums)
print(idx_num_pair)

words = ['안녕하세요', '제', '이름은', '비밀']
word_lengths = {name: len(name) for name in words}
print(word_lengths)  # {'안녕하세요': 5, '제': 1, '이름은': 3, '비밀': 2}

implicit_expr = (x for x in [1, 2, 3, 4, 5])
print(implicit_expr)    # <generator object <genexpr> at 0x00000289750179E0>

# print(tuple(implicit_expr))     # (1, 2, 3, 4, 5)
# print(tuple(implicit_expr))     # ()
# print(list(implicit_expr))      # [1, 2, 3, 4, 5]
# print(set(implicit_expr))       # {1, 2, 3, 4, 5}
# print(dict(implicit_expr))

one_tuple = tuple([1])
print(*one_tuple)

comp_tuple = *(n for n in range(5)),
print(comp_tuple)       # (0, 1, 2, 3, 4)
print(type(comp_tuple)) # <class 'tuple'>
