#write a function to count how many times a specific element appears in a list
def count_element(lst, element):
    return lst.count(element)

print(count_element([1, 2, 2, 3, 4, 4, 5], 2))