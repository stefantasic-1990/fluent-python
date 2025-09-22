# 005: Second Largest Element
#
# Given a list of integers, return the second largest element.
# You must do this in one pass, using O(1) extra space.
# Do not use sorted(), max(), or any other helper functions.

input = [3, 1, 4, 7, 5, 9]

def solve(int_list: list[int]) -> int:
    first = second = None
    for n in int_list:
        if first is None or n > first:
            second = first
            first = n
        elif n != first and (second is None or n > second):
            second = n
    return second

solution = solve(input)
print(solution)

# This one is tricky.
#
# Learned that condition order matters:
# Python and/or use short-circuit evaluation, meaning that
# if you do 'if first is None or n > first', the first condition
# will short-circuit the second, meaning the second won't run.
# If it did, it would fail due to NoneType comparison with an int.
#
# Here initializing first and second to 0 is a bad move.
# It means that there are already assumed first and second values.
# Therefore if the input array is all negative, nothing will happen.
# Because a 0 is greater than any negative number.