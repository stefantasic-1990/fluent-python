# 008: Merge Two Sorted Lists
#
# You are given two independently sorted integer lists, a and b.
# Merge them into a single sorted list and return the result.
# Do not use any built-in sort functions or libraries.

a = [1, 3, 5]
b = [2, 4, 6, 8]

def solve(list_a: list[int], list_b: list[int]) -> list[int]:
    c = []
    i = j = 0
    while i < len(list_a) and j < len(list_b):
        if list_a[i] <= list_b[j]:
            c.append(list_a[i])
            i += 1
        elif list_a[i] > list_b[j]:
            c.append(list_b[j])
            j += 1
    c.extend(list_a[i:])
    c.extend(list_b[j:])

    return c

solution = solve(a, b)
print(solution)