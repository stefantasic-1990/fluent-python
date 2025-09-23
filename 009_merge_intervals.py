# 009: Merge Interrvals
#
# You're given a list of intervals, where each interval is represented 
# as a list of two integers [start, end].
#
# Merge all overlapping intervals and return a new list of non-overlapping
# intervals that cover all the intervals in the input.

intervals = [[1, 3], [8, 15], [2, 6], [15, 18]]

def solve(invals: list[list]) -> list[list]:
    i = 0
    invals.sort(key=lambda x: x[0])

    while i < (len(invals) - 1):
        if invals[i][1] >= invals[i+1][1]:
            invals.pop(i+1)
        elif invals[i][1] >= invals[i+1][0]:
            invals[i][1] = invals[i+1][1]
            invals.pop(i+1)
        else:
            i += 1

    return invals

solution = solve(intervals)
print(solution)