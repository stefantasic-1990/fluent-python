# 007: Second Largest Element
#
# Given an array of integers nums and an integer target,
# return the indices of the two numbers such that they add up to the target.
# 
# You may assume that each input has exactly one solution,
# and you may not use the same element twice.
# 
# Return the answer as a list of two indices.
# The order does not matter.

input = [1, 2, 7, 10]
tgt = 9

def solve(num_list: list[int], target: int) -> bool:
    a = 0
    b = 0
    for i in range(len(num_list) - 1):
        for j in range(i + 1, len(num_list)):
            if num_list[i] + num_list[j] == tgt:
                return [i, j]
    return []

# The above is the O(n^2) version.
# The below is O(n), an improvement

def solve2(num_list: list[int], target: int) -> bool:
    seen = {} # You want a dict because you need to track the index

    for i, num in enumerate(num_list):
        complement = target - num
        if complement in seen:
            return [i, seen[complement]]
        seen[num] = i
    return []

solution = solve2(input, tgt)
print(solution)

# This improvement reduces the time complexity because:
# It capitalizes on storing accessed values for reference.
# This is instead of looping forward through them again and again.
# You are "looking backward" to what was already seen as you iterate.