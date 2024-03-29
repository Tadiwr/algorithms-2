def valid_parenthesis(s: str) -> bool:
    stack = []
    openings = ['{', '[', '(']
    closings = ['}', ']', ')']


    for c in s:
        if c in openings:
            stack.append(c)
        else:
            expected_opening_bracket = openings[closings.index(c)]

            try:
                if not stack.pop() == expected_opening_bracket:
                    return False
            except IndexError:
                return False

    return len(stack) == 0

print(valid_parenthesis('){'))