# 014: First Missing Positive Integer
#
# Given an unsorted integer array nums, return the smallest missing positive integer.
# You must solve this in O(n) time and O(1) extra space (i.e., in-place).
#
# Do not use extra hash sets or dicts.
# Do not use any sort functions.

nums = [5, 2, 0, 3, 1]

def solve(nums: list[int]) -> int:
    for i in range(len(nums)):
        while 1 <= nums[i] <= len(nums) and nums[i] != nums[nums[i] - 1]:
            j = nums[i] - 1
            nums[i], nums[j] = nums[j], nums[i]

    for i in range(len(nums)):
        if nums[i] != i + 1:
            return i + 1

    return len(nums) + 1

print(solve(nums))