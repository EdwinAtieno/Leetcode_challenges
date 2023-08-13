def valid_braces(string: str) -> bool:
    stack = []
    for c in string:
        if c in ["(", "[", "{"]:
            stack.append(c)
        elif c == ")":
            if not stack or stack.pop() != "(":
                return False
        elif c == "]":
            if not stack or stack.pop() != "[":
                return False
        elif c == "}":
            if not stack or stack.pop() != "{":
                return False
    return not stack
