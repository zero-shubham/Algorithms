def is_operator(val):
    if val == "+" or val == "-" or val == "/" or val == "*" or val == "(" or val == ")":
        return True
    return False


def fix_double_digits(infix_expr):
    for idx, _ in enumerate(infix_expr):
        if idx+1 < len(infix_expr) and not is_operator(
            infix_expr[idx]
        ) and not is_operator(
            infix_expr[idx+1]
        ):
            tmp = infix_expr[idx] + infix_expr[idx+1]
            infix_expr.pop(idx+1)
            infix_expr[idx] = tmp
    return infix_expr


def check_priority_of_val(val, stack_val):
    pri_list = ["(", ")", "*", "/", "+", "-"]
    idx = pri_list.index(val)
    if stack_val in pri_list[0: idx]:
        return "lower"
    else:
        return "higher"


def add_to_stack(val, stack, postfix):
    if val == ")":
        for idx in range(len(stack)-1, 0, -1):
            if stack[idx] != "(":
                popped = stack.pop()
                postfix.append(popped)
            else:
                stack.pop()
                break
        return
    for v in stack:
        priority = check_priority_of_val(val, v)
        # if val to be added has lower priority compared to
        # last value of the stack, pop the last val
        if priority == "lower":
            popped = stack.pop()
            postfix.append(popped)
        else:
            break
    stack.append(val)


def to_postfix(infix_expr):
    infix_expr = list(infix_expr)
    stack = []
    postfix = []
    infix_expr = fix_double_digits(infix_expr)

    for val in infix_expr:
        if not is_operator(val):
            postfix.append(val)
        else:
            add_to_stack(val, stack, postfix)
    stack = reversed(stack)
    postfix.extend(stack)
    return postfix