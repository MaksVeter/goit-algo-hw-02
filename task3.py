def is_balanced(expression):
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}
    opening_brackets = set(mapping.values())
    closing_brackets = set(mapping.keys())

    for char in expression:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack:
                return "Несиметрично"
            top_element = stack.pop()
            if mapping[char] != top_element:
                return "Несиметрично"

    if not stack:
        return "Симетрично"
    else:
        return "Несиметрично"


print(is_balanced("( ){[ 1 ]( 1 + 3 )( ){ }}"))  # +
print(is_balanced("( 23 ( 2 - 3);"))  # -
print(is_balanced("( 11 }"))  # -
