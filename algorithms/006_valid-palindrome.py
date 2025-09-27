# 006: Valid Palindrome
#
# Given a string s, determine if it is a palindrome, considering only
# alphanumeric characters and ignoring case.
# 
# Conditions:
# 
# 1. Ignore all non-alphanumeric characters (like spaces, punctuation, etc.)
# 2. Do not use built-in string split/reverse functions.

s = "A man, a plan, a canal: Panama"

def solve(s: str) -> bool:
    s_list = list(s.lower())
    alphanums = (
        {chr(c) for c in range(ord("a"), ord("z") + 1)} |
        {chr(c) for c in range(ord("0"), ord("9") + 1)}
    )
    i = 0
    j = len(s) - 1

    while i < j:
        if s_list[i] not in alphanums:
            i += 1
        elif s_list[j] not in alphanums:
            j -= 1
        elif s_list[i] == s_list[j]:
            i += 1
            j -= 1
        else:
            return False

    return True

print(solve(s))