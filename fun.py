class Calculator:
    def addition(self, a, b):
        return a + b

    def subtraction(self, a, b):
        return a - b

    def multiplication(self, a, b):
        return a * b

    def division(self, a, b):
         return a / b

    def cube(self, a):
        return a ** 3
obj = Calculator()
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Cube")

choice = int(input("Enter your choice: "))

match choice:
    case 1:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        result = obj.addition(a, b)

    case 2:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        result = obj.subtraction(a, b)

    case 3:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        result = obj.multiplication(a, b)

    case 4:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        result = obj.division(a, b)

    case 5:
        a = int(input("Enter number: "))
        result = obj.cube(a)

    case _:
        result = "Invalid Choice"

print("Answer =", result)
