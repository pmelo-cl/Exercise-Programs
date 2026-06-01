def bracket_validator(s: str) -> bool:
    stack = []

    for character in s:
        if character in "{[(":
            stack.append(character)
        if character in "}])":
            if not stack:
                return False
            braquet = stack.pop()
            if character == "}" and braquet != "{":
                return False
            elif character == ")" and braquet != "(":
                return False
            elif character == "]" and braquet != "[":
                return False

    return not stack


print(bracket_validator("()"))                         # → True
print(bracket_validator("()[]{}"))                     # → True
print(bracket_validator("{[()]}"))                     # → True
print(bracket_validator(""))                           # → True
print(bracket_validator("hello(hhhh)world{ho}w are"))  # → True
print(bracket_validator("(]"))                         # → False
print(bracket_validator("([)]"))                       # → False
print(bracket_validator("((("))                        # → False
print(bracket_validator("())"))                        # → False
