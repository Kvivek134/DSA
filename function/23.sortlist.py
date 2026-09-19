#write a function to sort list without using sort function
def sort_list(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst
print(sort_list([5, 2, 9, 1, 5, 6]))