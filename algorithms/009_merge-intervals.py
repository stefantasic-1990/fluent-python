# 009: Merge Interrvals
#
# You're given a list of intervals, where each interval is represented 
# as a list of two integers [start, end].
#
# Merge all overlapping intervals and return a new list of non-overlapping
# intervals that cover all the intervals in the input.

intervals = [[2, 6], [1, 3], [15, 18], [8, 15]]

def solve(intervals: list[list[int]]) -> list[list[int]]:
    j = 0
    intervals.sort()

    for i in range(1, len(intervals)):
        if intervals[j][1] >= intervals[i][0]:
            intervals[j][1] = max(intervals[j][1], intervals[i][1])
        else:
            j += 1
            intervals[j] = intervals[i]

    return intervals[:j+1]

print(solve(intervals))