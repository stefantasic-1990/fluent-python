# 003: Manual Frequency Count of Chars
#
# Given a string, reverse the words in the sentence.
# Return the reversed sentence as a string with no extra white space.
# You must not use str.split() or any built-in word-tokenizing shortcuts.

s = "  the sky  is  blue "

def solve1(s: str) -> str:
    word = []
    words = []
    for ch in s:
        if ch != " ":
            word.append(ch)
        elif word:
            words.append("".join(word))
            word.clear()
    if word:
        words.append("".join(word))

    return " ".join(reversed(words))
    
print(solve1(s))

# Easy to forget to add the last word if the string does not end in a space.
# No need to check if word exists but this is more intentional and cleaner.
# Otherwise, the words list can contain an empty string at the end (doesn't break the return value).