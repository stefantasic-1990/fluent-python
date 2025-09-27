# 001: Remove Duplicates From Sorted Array
#
# Given an integer array 'nums' sorted in non-decreasing order, remove 
# the duplicates in-place such that each unique element appears only once.
#
# The relative order should be kept the same.
# Return the list of unique elements in nums.
# You must do this in O(1) space (in-place).

nums = [3, 3, 6, 7, 23, 23, 27]

def solve1(nums: list[int]) -> list[int]:
    i = 1
    while i < len(nums):
        if nums[i] == nums[i-1]:
            del nums[i-1]
        else:
            i += 1

    return nums

# The above version works but:
#
# Every del costs O(n) because the list elements need to be shifted left.
# This means that with a lot of duplicates, the time complexity can go to O(n^2).

def solve2(nums: list[int]) -> list[int]:
    i = 0
    j = 0
    while j < len(nums):
        if nums[j] > nums[i]:
            i += 1
            nums[i] = nums[j]
        j += 1

    return nums[:i+1]

print(solve2(nums))

# This modifies the list in place, avoiding the moving over of elements on delete.
# This version has a time complexity of O(n): single scan, no costly delete shifting.
# Can set j=1 to skip the redundant first element compare with itself and add an explicit guard...
# but having j=0 protects against the edge case of an empty list with fewer lines, which I prefer.