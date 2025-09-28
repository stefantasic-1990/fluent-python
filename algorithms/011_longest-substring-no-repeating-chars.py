# 011: Longest Substring Without Repeating Characters
#
# Given a string, find the length of the longest substring without repeating characters.
# You must solve it in O(n) time. Don’t use .split(), or any substring tricks that hide complexity.

s = "abcabcbb"

def solve(s: str) -> int:
    window = set()
    max_len = 0
    right = left = 0

    while right < len(s):
        if s[right] not in window:
            window.add(s[right])
            max_len = max(max_len, len(window))
            right += 1
        else:
            while s[right] in window:
                window.remove(s[left]) 
                left += 1

    return max_len

print(solve(s))