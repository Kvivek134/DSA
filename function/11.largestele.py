#write a function to find largest element in a list
def largest_element(lst):
    if not lst:
        return None
    largest = lst[0]
    for num in lst:
        if num > largest:
            largest = num
    return largest

print(largest_element([1, 5, 3, 9, 2]))