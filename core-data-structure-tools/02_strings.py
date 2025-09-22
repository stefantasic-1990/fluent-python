print("-----basic string traversal pattern-----")
# basic string traversal
#
# use to scan a string from beginning to end and do something with each character
# only use range if you need to do something relative to each position, otherwise use "c in s"
s = "useless string"

for i in range(len(s)):
    print(s[i])

print("-----substring slicing-----")
# substring slicing
#
# use to slice out a continuous piece of a string
s = "sdjdjswordjsj"

ss = s[5:10] # omits the last character index
print(ss)

print("-----manual string splitting-----")
# manual string splitting
#
# use to split a string into a list of substrings based on a given character separator
s = "this is a string"
word = ""
words = []
separator = " "

for c in s:
    if c != separator:
        word += c
    else:
        if word:
            words.append(word)
            word = ""
if word:
    words.append(word)
print(words)

print("-----string reversal in place-----")
# string reversal in place
#
# use to reverse a string in place

s = "reverse me in place please"
s = list(s) # convert to a list so that you can move characters around - strings are immutable

l = 0
r = len(s) - 1

while l < r:
    s[l], s[r] = s[r], s[l] # tuple unpacking lets you swap two variables in one line, no temp variable needed
    l += 1
    r -= 1
s = "".join(s)
print(s)