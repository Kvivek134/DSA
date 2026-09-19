#write a function to find the maximum of two numbers
def max_of_two(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

result = max_of_two(5, 3)
print(result)