print("-----frequency count-----")
# frequency count
#
# a pattern to count the frequency items in an iterable
s = "abcdaadce"
frequencies = {}

for c in s:
    if c not in frequencies:
        frequencies[c] = 0
    frequencies[c] += 1
print(frequencies)

print("-----first unique character position in string-----")
# first unique character position in string
#
# a pattern to find the first unique character in a string
# first build a frequency map, then scan it to find the first char position with frequency of 1
s = "abcdaadce"
frequencies = {}

for c in s:
    if c not in frequencies:
        frequencies[c] = 0
    frequencies[c] += 1

for i, c in enumerate(s):
    if frequencies[c] == 1:
        break
print(i)

print("-----check for duplicates-----")
# check for duplicates
#
# a pattern to check for duplicates in an iterable
s = "do i have a duplicate"

seen = set()
for c in s:
    if c != " " and c in seen:
        print(f"the duplicate is {c}")
        break
    seen.add(c)