from copy import deepcopy

nums = [[1, 2], [3, 4]]
cp1 = deepcopy(nums)
cp2 = nums[:]

cp1[0][0] = -1
print(f'{nums[0][0]=}')     # nums[0][0]=1

cp2[0][0] = -1
print(f'{nums[0][0]=}')     # nums[0][0]=-1

