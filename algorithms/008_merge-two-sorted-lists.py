# 008: Merge Two Sorted Lists
#
# You are given two sorted integer lists, a and b.
# Merge them into a single sorted list and return the result.
# Do not use any built-in sort functions or libraries.

list_a = [1, 3, 5]
list_b = [2, 4, 6, 8]

def solve(list_a: list[int], list_b: list[int]) -> list[int]:
    result = []
    i = j = 0

    while i < len(list_a) and j < len(list_b):
        if list_a[i] <= list_b[j]:
            result.append(list_a[i])
            i += 1
        else:
            result.append(list_b[j])
            j += 1

    result.extend(list_a[i:])
    result.extend(list_b[j:])

    return result

print(solve(list_a=list_a, list_b=list_b))