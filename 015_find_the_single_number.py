# 014: First Missing Positive Integer
#
# You are given a non-empty list of integers nums.
# Every element appears twice, except for one element, which appears only once.
#
# Return that single element.

nums = [4, 1, 2, 1, 2]

def solve(nums: list[int]) -> int:
    result = 0
    for n in nums:
        result ^= n
    return result

solution = solve(nums=nums)
print(solution)

# This is elegant.