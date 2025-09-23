from collections import deque

print("-----stack/LIFO-----")
# stack/LIFO
#
# tools to manage an array as a stack
stack = []
stack.append("a")
top = stack.pop()
print(top)

print("-----queue/FIFO-----")
# queue/FIFO
#
# tools to manage a double ended queue list
x = "a"
q = deque()
q.append(x)
x = q.popleft()
print(x)

# balaced brackets algorithm
#
# tool to ensure a string has balanced brackets - all opened are closed
s = "(x+y*(a+2)"
stack = []

for c in s:
    if c == "(":
        stack.append(c)
    elif c == ")":
        if not stack:
            print("Fail")
        stack.pop()
if stack:
    print("Fail")
else:
    print("Pass")