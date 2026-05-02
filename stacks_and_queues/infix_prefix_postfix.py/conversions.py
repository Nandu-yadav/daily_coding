def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    if op == '^':
        return 3
    return 0

def infix_to_prefix(infix):
    # Step 1: reverse infix
    infix = infix[::-1]

    # Step 2: swap brackets
    infix = infix.replace('(', '#')
    infix = infix.replace(')', '(')
    infix = infix.replace('#', ')')

    stack = []
    result = []

    for ch in infix:
        # Operand
        if ch.isalnum():
            result.append(ch)

        # Left parenthesis
        elif ch == '(':
            stack.append(ch)

        # Right parenthesis
        elif ch == ')':
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()

        # Operator
        else:
            while (stack and
                   precedence(ch) < precedence(stack[-1])):
                result.append(stack.pop())
            stack.append(ch)

    while stack:
        result.append(stack.pop())

    # Step 4: reverse postfix → prefix
    return ''.join(result[::-1])


# Example
expr = "(A-B/C)*(A/K-L)"
print("Prefix:", infix_to_prefix(expr))
