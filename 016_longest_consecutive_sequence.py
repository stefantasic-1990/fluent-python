# 015: Longest Consecutive Sequence
#
# You are given an unsorted list of integers nums.
# Return the length of the longest consecutive elements sequence.
# 
# You must solve it in O(n) time.
# No sorting allowed.
# You must use O(n) time.
# Do not use the same number twice.
# Duplicates may exist, but they don’t count toward the sequence.

nums = [100, 4, 200, 1, 3, 2]

def solve(nums: list[int]) -> int:
    max_len = 0
    nums_set = set(nums)
    for n in nums:
        len = 0
        while n + len in nums_set:
            max_len = max(max_len, len)

    return max_len

solution = solve(nums=nums)
print(solution)