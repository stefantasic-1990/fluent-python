ops = "4 5 DUP POP 6 - 7 +"

def get_top_int(stack):
    for item in reversed(stack):
        if item.isdigit():
            return item
    return -1

def del_top_int(stack):
    for i in range(len(stack)-1, -1, -1):
        if stack[i].isdigit():
            stack.pop(i)
            return
    return -1

def pop_top_int(stack):
    for i in range(len(stack)-1, -1, -1):
        if stack[i].isdigit():
            item = stack.pop(i)
            return item
    return -1

def solution(S):
    token_list = S.split()
    stack = []

    min_int_val = 0
    max_int_val = 1048575

    for token in token_list:
        print(stack)
        if token.isdigit() and min_int_val <= int(token) <= max_int_val:
            stack.append(token)
        elif token == "POP":
            del_top_int(stack)
        elif token == "DUP":
            top_int = get_top_int(stack)
            stack.append(top_int)
        elif token == "+":
            add_1 = int(pop_top_int(stack))
            add_2 = int(pop_top_int(stack))
            add_result = add_1 + add_2
            if min_int_val <= add_result <= max_int_val:
                stack.append(str(add_result))
            else:
                return -1
        elif token == "-":
            sub_1 = int(pop_top_int(stack))
            sub_2 = int(pop_top_int(stack))
            sub_result = sub_1 - sub_2
            if min_int_val <= sub_result <= max_int_val:
                stack.append(str(sub_result))
            else:
                return -1
    
    result = int(get_top_int(stack))
    print(result)
    return result

# using isdigit() is not the most efficient approach, since it needs me to
# convert the ints back to string representation after adding/subtracting them
# probably won't have time to refine this as I'm working against.. time..