# Arithmetic Operations Program without using functions

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /, %): ")

if operator == '+':
    print("Addition:", num1 + num2)
elif operator == '-':
    print("Subtraction:", num1 - num2)
elif operator == '*':
    print("Multiplication:", num1 * num2)
elif operator == '/':
    if num2 == 0:
        print("Cannot divide by zero")
    else:
        print("Division:", num1 / num2)
elif operator == '%':
    if num2 == 0:
        print("Cannot divide by zero")
    else:
        print("Remainder:", num1 % num2)
else:
    print("Invalid operator")
