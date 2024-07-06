def merge_sorted_lists(list1, list2):
    merged_list = []
    i = 0  # index for list1
    j = 0  # index for list2
    
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1
    
    # Add remaining elements of list1, if any
    while i < len(list1):
        merged_list.append(list1[i])
        i += 1
    
    # Add remaining elements of list2, if any
    while j < len(list2):
        merged_list.append(list2[j])
        j += 1
    
    return merged_list

# Example usage:
list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 6, 8, 10]
merged_list = merge_sorted_lists(list1, list2)
print("List 1:", list1)
print("List 2:", list2)
print("Merged Sorted List:", merged_list)
