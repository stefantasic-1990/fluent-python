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

def solve(string: list[int], target: int) -> bool:
    a = 0
    b = 0
    for i in range(len(string) - 1):
        for j in range(i + 1, len(string)):
            if string[i] + string[j] == tgt:
                return [i, j]
    return []

solution = solve(input, tgt)
print(solution)