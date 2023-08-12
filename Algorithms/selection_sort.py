# Selection Sort

# Repeatedly selecting the minimum (or maximum) element 
# from the unsorted part of the array and 
# placing it at the beginning of the sorted part

# Time Complexity: O(n^2) Quadratic
# Inefficent for large arrays

def selection_sort(arr):
    n = len(arr)
    
    # Outer loop - defines the boundary between sorted and unsorted parts
    for i in range(n -1): # loop through the array until the last element (n -1)
        min_index = i # Assume the current index holds the lowest number

        # Inner loop - searches for the smallest element in the unsorted loop 
        # Find the index of the smallest element in the remaining unsorted section
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j # keep track of the index of the smallest element found
                
        # Swap the minumum number with the element at the current position        
        arr[i], arr[min_index] = arr[min_index], arr[i]
        
# Provide the array
arr = [34, 54, 76, 22, 45, 6, 12, 98, 43, 67, 55]
selection_sort(arr) #run the function
print(f'This is the selected array:', arr)