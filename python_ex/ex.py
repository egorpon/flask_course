def func(nums):
    return [n**2 for n in nums[0::2]][::-1]

print(func([1, 2, 3, 4, 5, 6, 7]))