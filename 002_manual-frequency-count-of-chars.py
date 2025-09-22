# 002: Manual Frequency Count of Chars
#
# Given a string, count how many times each character appears.
# Return a dictionary where keys are characters and values are frequencies.

input = "banana"

def solve(string: str) -> dict[str, int]:
    freqs = {}
    for c in string:
        if c not in freqs:
            freqs[c] = 0
        freqs[c] += 1

    return freqs

solution = solve(input)
print(solution)