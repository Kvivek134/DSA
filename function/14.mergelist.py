#write a function to merge two lists and removes duplicates
def merge_lists(lst1, lst2):
    merged_list = lst1 + lst2
    return list(set(merged_list))
print(merge_lists([1, 2, 3], [3, 4, 5]))