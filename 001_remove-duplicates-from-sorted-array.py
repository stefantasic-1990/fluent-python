# 001: Remove Duplicates From Sorted Array
#
# Given an integer array 'nums' sorted in non-decreasing order, remove 
# the duplicates in-place such that each unique element  appears only once.
# The relative order should be kept the same. Return the number of unique
# elements in nums. You must do it in O(1) extra memory (in-place).

input = [1, 1, 2, 2, 3]

def solve(arr: list[int]) -> int:
    i = 0
    for j in range(1, len(arr)):
        if arr[j] != arr[i]:
            i += 1
            arr[i] = arr[j]
    unique_count = i + 1
    return unique_count

solution = solve(input)
print(solution)