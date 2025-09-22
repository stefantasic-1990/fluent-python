print("-----basic array traversal pattern-----")
# basic array traversal pattern
#
# use to scan array elements from beginning to end and do something with them
arr = [1, 2, 3, 4, 5, 6]

for i in range(len(arr)):
    print(arr[i])

print("-----two pointer traversal pattern-----")
# two pointer traversal pattern
#
# use to scan for pairs, subarrays, deduplicate in place etc.
# below case deduplicates in place and returns the new array length
arr = [1, 2, 2, 4, 5, 5, 6]
i = 0

for j in range(1, len(arr)):
    if arr[j] != arr[i]:
        i += 1
        arr[i] = arr[j]
    new_len = i + 1
print(new_len)

print("-----sliding window traversal pattern-----")
# sliding window traversal pattern
#
# use to find max/min/frequency in substrings/subarrays
# below case finds the longest substring length without repeating characters
s = "abceabcbb"
seen = set()
l = 0
max_len = 0

for r in range(len(s)):
    while s[r] in seen:
        seen.remove(s[l])
        l += 1
    seen.add(s[r])
    max_len = max(max_len, r - l + 1)
print(max_len)