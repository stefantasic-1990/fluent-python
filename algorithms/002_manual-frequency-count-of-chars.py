# 002: 002: Manual Frequency Count of Chars
#
# Given a string, count how many times each character appears.
# Return a dictionary where keys are characters and values are frequencies.

s = "banana"

def solve1(s: str) -> dict[str, int]:
    freqs = {}
    for ch in s:
        freqs[ch] = freqs.get(ch, 0) + 1

    return freqs

print(solve1(s))

# Using .get(key, default) ensures that a dict key entry that doesn't exist is initialized.
# Another way is to explicitly check if an explicit if block, but that requires two lines.