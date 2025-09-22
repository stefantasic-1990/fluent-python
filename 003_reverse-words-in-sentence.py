# 003: Manual Frequency Count of Chars
#
# Given a string, reverse the words in the sentence.
# Return the reversed sentence as a string.
# You must not use str.split() or any built-in word-tokenizing shortcuts.

input = "  the sky  is  blue "

def solve(string: str) -> str:
    words = []
    word = []

    for c in string:
        if c == " ":
            if word:
                words.append("".join(word))
                word = []
        else:
            word.append(c)
    if word:
        words.append("".join(word))

    i = 0
    j = len(words) - 1

    while i < j:
        words[i], words[j] = words[j], words[i]
        i += 1
        j -= 1

    rev_string = " ".join(words)

    return rev_string
    
solution = solve(input)
print(solution)