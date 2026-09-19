#write a function that accept any number of arguments using *args
def sum_of_numbers(*args):
    return sum(args)

print(sum_of_numbers(1, 2, 3, 4, 5))