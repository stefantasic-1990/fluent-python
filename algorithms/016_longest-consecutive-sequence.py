# 016: Longest Consecutive Sequence
#
# You are given an unsorted list of integers nums.
# Return the length of the longest consecutive elements sequence.
# 
# You must solve it in O(n) time.
# No sorting allowed.
# Do not use the same number twice.
# Duplicates may exist, but they don’t count toward the sequence.

nums = [100, 4, 200, 1, 3, 2]

def solve(nums: list[int]) -> int:
    nums_set = set(nums)
    longest_seq = 0

    for n in nums_set:
        if n - 1 not in nums_set:
            current_num = n
            current_seq = 1
            while current_num + 1 in nums_set:
                current_seq += 1
                current_num += 1
            longest_seq = max(current_seq, longest_seq)

    return longest_seq

print(solve(nums))