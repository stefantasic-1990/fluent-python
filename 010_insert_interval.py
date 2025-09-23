# 010: Insert Interrval
#
# You're given:
# 
# 1. A list of non-overlapping, sorted intervals intervals (each is a list[start, end])
# 2. A new interval [new_start, new_end] that may overlap with one or more intervals in intervals.
# 
# Insert the new interval into the correct position and merge any overlapping intervals.
# Return the result as a new list.

intervals = [[1, 3], [6, 9]]
new_interval = [2, 5]

def solve(invals: list[list], new_inval: list[int]) -> list[list]:
    if new_inval[0] > invals[len(invals)-1][0]:
        invals.insert(len(invals), new_inval)
    else:
        for i in range(len(invals)):
            if new_inval[0] <= invals[i][0]:
                invals.insert(i, new_inval)
                break

    k = 0
    while k < (len(invals) - 1):
        if invals[k][1] >= invals[k+1][1]:
            invals.pop(k+1)
        elif invals[k][1] >= invals[k+1][0]:
            invals[k][1] = invals[k+1][1]
            invals.pop(k+1)
        else:
            k += 1

    return invals

solution = solve(intervals, new_interval)
print(solution)