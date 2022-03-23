"""
module: math
description: mathematics related basic operations
"""

def addition(num1, num2):
    """
    adds the two numbers and return addition
    input:  two numbers
    return: addition of input numbers
    """
    return num1+num2


if __name__ == "__main__":
    a, b = 10, 20
    ADDITION = addition(a, b)
    print(f"addition of {a} and {b} is: {ADDITION}")
    a, b = 20, 30
    ADDITION = addition(a, b)
    print(f"addition of {a} and {b} is: {ADDITION}")
