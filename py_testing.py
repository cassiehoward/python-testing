def replace_vowels(content, ch):
    vowels = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']
    if content is None or ch is None:
        return "Invalid input :("
    result = []
    for char in content:
        if char in vowels:
            result.append(ch)
        else:
            result.append(char)
    return ''.join(result)


class DivisionByZeroError(Exception):
    pass


def calculator(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        if b == 0:
            # raise ValueError("Cannot divide by zero")
            # raise DivisionByZeroError("Cannot divide by zero")
            assert b != 0, "Cannot divide by zero"
        return a / b
    else:
        raise ValueError("Invalid operation")


print(calculator(8, 2, "+"))
