# 011: Longest Substring Without Repeating Characters
#
# Given a string, find the length of the longest substring without repeating characters.
# You must solve it in O(n) time. Don’t use .split(), or any substring tricks that hide complexity.

s = "abcabcbb"

def solve(s: str) -> int:
    window = set()
    max_len = 0
    i = j = 0

    while i < len(s):
        if s[i] not in window:
            window.add(s[i])
            i += 1
            max_len = max(max_len, i - j)
        else:
            while s[i] in window:
                window.remove(s[j]) 
                j += 1

    return max_len

print(solve(s))