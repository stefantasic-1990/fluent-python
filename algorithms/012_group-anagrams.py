# 012: Group Anagrams
#
# Given a list of strings, group the anagrams together.
# Return the groups as a list of lists

anagrams = ["eat", "tea", "tan", "ate", "nat", "bat"]

def solve(anagrams: list[str]) -> list[list[str]]:
    anagrams_map = {}

    for word in anagrams:
        counts = [0] * 26
        for ch in word:
            counts[ord(ch) - ord("a")] += 1
        key = tuple(counts)
        if key not in anagrams_map:
            anagrams_map[key] = []
        anagrams_map[key].append(word)

    return list(anagrams_map.values())

print(solve(anagrams))