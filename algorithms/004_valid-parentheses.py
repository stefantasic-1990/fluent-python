# 004: Valid Parentheses
#
# Given a string s containing only (, ), {, }, [, ] 
# determine if the input string is valid.
# A string is valid if:
#
# 1. Open brackets are closed by the same type of brackets.
# 2. Open brackets are closed in the correct order.

s = "[]"

def solve(s: str) -> bool:
    bracket_map = {
        ")": "(",
        "]": "[",
        "}": "{",
    }
    bracket_stack = []
    open_brackets = set(bracket_map.values())
    
    for b in s:
        if b in open_brackets:
            bracket_stack.append(b)
        elif b in bracket_map:
            if bracket_stack and bracket_map[b] == bracket_stack[-1]:
                bracket_stack.pop()
            else:
                return False

    return not bracket_stack

print(solve(s))

# Creating an `open_brackets`` variable allows us to avoid re-scanning dict values each iteration