# 017: Longest Repeating Character Replacement
#
# You are given a string s and an integer k.
# You may replace at most k characters in the string so that all the characters in some substring are the same.
# Return the length of the longest such substring you can create.

s = "AABABBABBAB"
k = 2

def solve(s: str, k: int) -> int:
    j = 0
    freqs = {}
    max_freq = 0
    longest = 0

    for i in range(len(s)):
        freqs[s[i]] = freqs.get(s[i], 0) + 1
        max_freq = max(freqs[s[i]], max_freq)

        if (i - j + 1) - max_freq > k:
            freqs[s[j]] = freqs.get(s[j], 0) - 1
            j += 1

        longest = max(i - j + 1, longest)

    return longest

print(solve(s, k))