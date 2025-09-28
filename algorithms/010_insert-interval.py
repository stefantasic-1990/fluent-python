# 010: Insert Interval
#
# You're given:
# 
# 1. A list of non-overlapping, sorted intervals intervals (each is a list[start, end])
# 2. A new interval [new_start, new_end] that may overlap with one or more intervals in intervals.
# 
# Insert the new interval into the correct position and merge any overlapping intervals.
# Return the result as a new list of non-overlapping sorted intervals.

intervals = [[1, 3], [6, 9]]
new_interval = [2, 5]

def solve(intervals: list[list[int]], new_interval: list[int]) -> list[list[int]]:
    result_intervals = []
    i = 0

    # append all the smaller intervals
    while i < len(intervals) and intervals[i][1] < new_interval[0]:
        result_intervals.append(intervals[i])
        i += 1

    # merge all overlapping intervals into one and append
    while i < len(intervals) and intervals[i][0] <= new_interval[1]:
        new_interval = [
            min(intervals[i][0], new_interval[0]), 
            max(intervals[i][1], new_interval[1])
        ]
        i += 1

    result_intervals.append(new_interval)
    result_intervals.extend(intervals[i:])

    return result_intervals

print(solve(intervals=intervals, new_interval=new_interval))