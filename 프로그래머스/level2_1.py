
def solution(nums):

    def get_max_linear(arr):
        temp_max = 0
        delay_max = 0
        dp = [0] * len(arr)

        for i, n in enumerate(arr):
            dp[i] = max(dp[i], delay_max + arr[i])
            delay_max = temp_max
            temp_max = max(dp[i], temp_max)

        return temp_max

    res1 = get_max_linear(nums[1:])
    res2 = get_max_linear(nums[:-1])

    return max(res1, res2)




args = [
    [[14, 6, 5, 11, 3, 9, 2, 10]],
    [[1, 3, 2, 5, 4]],
    [[1]],
]

sols = [
    36,
    8,
    1
]

for a, s in zip(args, sols):
    res = solution(*a)
    if res != s:
        print(f'result {res} differ from {s}')

print('test finished')