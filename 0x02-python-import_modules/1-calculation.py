#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, subtract, multiply, divide

    a = 10
    b = 5

    addition_result = add(a, b)
    subtraction_result = subtract(a, b)
    multiplication_result = multiply(a, b)
    division_result = divide(a, b)

    print("Result of addition:", addition_result)
    print("Result of subtraction:", subtraction_result)
    print("Result of multiplication:", multiplication_result)
    print("Result of division:", division_result)
