# 012: Group Anagrams
#
# Given a list of strings, group the anagrams together.
# Return the groups as a list of lists

input = ["eat", "tea", "tan", "ate", "nat", "bat"]

def solve(anagrams: list[str]) -> list[list[str]]:
    anagrams_dict = {}
    for word in anagrams:
        key = "".join(sorted(word))
        if key not in anagrams_dict:
            anagrams_dict[key] = []
        anagrams_dict[key].append(word)
    anagram_lists = [anagrams_dict[key] for key in anagrams_dict]
    return anagram_lists

solution = solve(input)
print(solution)