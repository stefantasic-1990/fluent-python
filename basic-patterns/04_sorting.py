print("-----find max manually-----")
# find max manually
#
# a pattern to find the max value manually without using max()
vals = [23, 125, 12, 365, 64, 53]
max_val = vals[0]

for x in vals[1:]:
    if x > max_val:
        max_val = x
print(max_val)

print("-----descending sorton a set by key-----")
# descending sorton a set by key
#
# a pattern to descending sort a list of sets by key
data = [('a', 2), ('b', 5), ('c', 3)]
data.sort(key=lambda x: (-x[1], x[0]))
print(data)