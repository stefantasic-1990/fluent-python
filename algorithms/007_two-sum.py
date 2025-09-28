# 007: Two Sum
#
# Given a list of integers and an integer target:
# return the indices of the two numbers in the list that add up to the target.
# 
# You may assume that each input has exactly one solution.
# You may not use the same element twice.
# 
# Return the answer as a list of two indices.
# The order does not matter.

ints = [1, 2, 10, 7, 4]
target = 9

def solve(ints: list[int], target: int) -> list[int]:
    ints_map = {}

    for i, num in enumerate(ints):
        complement = target - num
        if complement in ints_map:
            return [ints_map[complement], i]
        ints_map[num] = i

    raise ValueError("No two numbers in list sum to target.")

print(solve(ints=ints, target=target))