# 006: Second Largest Element
#
# Given a string s, determine if it is a palindrome, considering only
# alphanumeric characters and ignoring case.
# 
# You must:
# 
# Ignore all non-alphanumeric characters (like spaces, punctuation, etc.)
# Do not use built-in string split/reverse functions.
# Use the two-pointer pattern: one from the left, one from the right.
# Compare characters manually, skipping non-alphanumerics.

input = "   "

def solve(string: str) -> bool:
    string = string.lower()
    alphanums = set(
        [chr(c) for c in range(ord('a'), ord('z') + 1)] +
        [chr(c) for c in range(ord('0'), ord('9') + 1)]
    )
    l_index = 0
    r_index = len(string) - 1
    while l_index < r_index:
        while string[r_index] not in alphanums and l_index < r_index:
            r_index -= 1
        while string[l_index] not in alphanums and l_index < r_index:
            l_index += 1
        if string[r_index] != string[l_index]:
            return False
        r_index -= 1
        l_index += 1
    return True

solution = solve(input)
print(solution)

# Learned how to create an alphanumeric set.