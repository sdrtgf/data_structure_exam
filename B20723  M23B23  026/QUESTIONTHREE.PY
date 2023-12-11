
 #Selection Sort
def selection_sort(unsorted_list):
    
    for i in range(len(unsorted_list)):
        # find the index of the minimum element in the remaining list
        min_index = i
        for j in range(i+1, len(unsorted_list)):
            if unsorted_list[j] < unsorted_list[min_index]:
                min_index = j
        
        unsorted_list[i], unsorted_list[min_index] = unsorted_list[min_index], unsorted_list[i]
    return unsorted_list

# Insertion Sort
def insertion_sort(unsorted_list):

    for i in range(1, len(unsorted_list)):
        key = unsorted_list[i]
        j = i-1
        
        while j >=0 and key < unsorted_list[j]:
            unsorted_list[j+1] = unsorted_list[j]
            j -= 1
        unsorted_list[j+1] = key
    return unsorted_list

# Unsorted List
unsorted_list = [14,27,8,-42,11,35,-9,56,23]

# Run the Sorting Algorithm
print("Unsorted List:", unsorted_list)

print("Selection Sort:")
sorted_list = selection_sort(unsorted_list.copy())
print("Sorted List:", sorted_list)

print("Insertion Sort:")
sorted_list = insertion_sort(unsorted_list.copy())
print("Sorted List:", sorted_list)
#Selection Sort and Insertion Sort have a time complexity of O(n^2) in the worst case scenario,
# as they require nested loops to iterate over each element in the list. They both have a space complexity of O(1)



