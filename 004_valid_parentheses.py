# 004: Valid Parentheses
#
# Given a string s containing only (, ), {, }, [ and ], 
# determine if the input string is valid.
# A string is valid if:
#
# 1. Open brackets are closed by the same type of brackets.
# 2. Open brackets are closed in the correct order.

input = "([)]"

def solve(string: str) -> bool:
    pairs = {")": "(", "]": "[", "}": "{"}
    brkt_stack = []
    for c in string:
        if c in ('(', '[', '{'):
            brkt_stack.append(c)
        elif c in (')', ']', '}') and brkt_stack:
            if pairs[c] == brkt_stack[-1]:
                brkt_stack.pop()
            else:
                return False
    return not brkt_stack

solution = solve(input)
print(solution)

# Note:
# Remember to always check for input edge cases.
# Here, on top of ensuring each bracket type closes itself,
# you also need to ensure that each bracket is closed,
# as well as ensuring that there are no unnecessary/extra closures.