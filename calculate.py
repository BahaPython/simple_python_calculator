# Advanced Calculator in Python
# This program allows the user to perform various mathematical operations

import math  # Importing math module for advanced functions like square root and power

def add(x, y):
    """Return the sum of x and y"""
    return x + y

def subtract(x, y):
    """Return the difference of x and y"""
    return x - y

def multiply(x, y):
    """Return the product of x and y"""
    return x * y

def divide(x, y):
    """Return the division of x by y"""
    if y == 0:
        return "Error: Division by zero is not allowed"
    return x / y

def power(x, y):
    """Return x raised to the power y"""
    return x ** y

def square_root(x):
    """Return the square root of x"""
    if x < 0:
        return "Error: Cannot take square root of negative number"
    return math.sqrt(x)

def percentage(x, y):
    """Return y percent of x"""
    return (x * y) / 100

def calculator():
    print("Welcome to Advanced Calculator!")
    print("Operations available:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (^)")
    print("6. Square Root (√)")
    print("7. Percentage (%)")

    while True:
        operation = input("Choose an operation (or 'q' to quit): ")

        if operation.lower() == 'q':
            print("Thank you for using the calculator!")
            break

        if operation in ('1', '2', '3', '4', '5', '7'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Error: Please enter valid numbers")
                continue

            if operation == '1':
                print("Result:", add(num1, num2))
            elif operation == '2':
                print("Result:", subtract(num1, num2))
            elif operation == '3':
                print("Result:", multiply(num1, num2))
            elif operation == '4':
                print("Result:", divide(num1, num2))
            elif operation == '5':
                print("Result:", power(num1, num2))
            elif operation == '7':
                print("Result:", percentage(num1, num2))

        elif operation == '6':
            try:
                num = float(input("Enter the number: "))
            except ValueError:
                print("Error: Please enter a valid number")
                continue
            print("Result:", square_root(num))

        else:
            print("Invalid operation! Please choose a valid one.")

# Run the calculator
calculator()