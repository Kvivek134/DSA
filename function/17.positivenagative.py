#write a function to check if a number is positive or negative or zero
def check_positive_negative(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"
print(check_positive_negative(5))