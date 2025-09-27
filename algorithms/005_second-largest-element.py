# 005: Second Largest Element
#
# Given a list of integers, return the second largest element.
# You must do this in one pass, using O(1) extra space.
# Do not use sorted(), max(), or any other helper functions.

ints = [5, 5]

def solve(ints: list[int]) -> int:
    first = float("-inf")
    second = float("-inf")
    
    for i in ints:
        if i > first:
            second = first
            first = i
        elif second < i < first:
            second = i
    if second == float("-inf"):
        return None

    return second

print(solve(ints))