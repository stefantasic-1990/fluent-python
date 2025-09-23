# 011: Longest Substring Without Repeating Characters
#
# Given a string, find the length of the longest substring without repeating characters.
# You must solve it in O(n) time. Don’t use .split(), or any substring tricks that hide complexity.

input = "abcabcbb"

def solve(s: str) -> str:
    subs = ""
    seen = set()
    i = k = 0
    while i < len(s):
        if s[i] not in seen:
            seen.add(s[i])
            i += 1
        else:
            if len(s[k:i]) > len(subs):
                subs = s[k:i]
            seen.remove(s[k])
            k += 1
    if len(s[k:i]) > len(subs):
        subs = s[k:i]

    return subs

solution = solve(input)
print(solution)

# Once you catch a duplicate, remove it from the seen set
# Then move the left end of the window forward, leave the right
# Let this happen again and again until the duplicate is remo

# This is a cleaner and more efficient version:

def solve2(s: str) -> str:
    seen = set()
    k = 0
    max_sub = ""

    for i in range(len(s)):
        while s[i] in seen:
            seen.remove(s[k])
            k += 1
        seen.add(s[i])
        if len(s[k:i+1]) > len(max_sub):
            max_sub = s[k:i+1]

    return max_sub