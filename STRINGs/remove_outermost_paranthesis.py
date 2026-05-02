

def removeOuterParentheses(s: str) -> str:
    result = []
    level = 0

    for ch in s:
        if ch == '(':
            level += 1
            if level > 1:
                result.append(ch)
        else:  # ch == ')'
            if level > 1:
                result.append(ch)
            level -= 1

    return "".join(result)
