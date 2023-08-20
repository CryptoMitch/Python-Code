# Merge Sort Algorithm

# Summary: Divide-and-conquer sorting algorithm. Break down lists into sublists and merge those lists back in

# Time Complexity: O(n log n)

# Space Complexity: O(n) 

def merge_sort(arr):
    
    # Base Case: for 0 or 1 elements in the array
    # if len(arr) <= 1
        # return arr
    
    # DIVIDE - Create Sublists
    # if the length of the array is greater than 1
    if len(arr) > 1:
        # Find the middle
        mid = len(arr) // 2
        # Divide the array into two lists
        left_half = arr[:mid] # Use slice notation to create left sublist
        right_half = arr[mid:] # Use slice notation to create right sublist
        
    # Recursively call the function to sort both lists
    # Run the algorithm until the sublists are considered sorted
    merge_sort(left_half)
    merge_sort(right_half)
    
    # MERGE/CONQUER - Merge the two lists
    
    # Initialise three viables to keep track of the positions
    left_index = 0 # Tracks the position in the left sublist
    right_index = 0 # Tracks the position in the right sublist
    merged_index = 0 # Tracks the position in merged as elements are chosen and merged into the arr, the merged_index is incremented to indicate the next available position in the merged array.
    
    while left_index < len(left_half) and right_index < len(right_half): # loop runs only when there are elements left to compare and merge.
        if left_half[left_index] < right_half[right_index]: # check which current element is smaller in each list
            arr[merged_index] = left_half[left_index] # Place the current element from the left_half into the merged array
            left_index += 1 # Move the left_index along by 1
        else:
            arr[merged_index] = right_half[right_index] # Place the current element from the right_half into the merged array
            right_index += 1 # Move the right_index along by 1
        merged_list += 1 # Move the merged_index along by 1 to indicate the next position in the merged array.
    
    # Left over elements need to be merged into the main list
    while left_index < len(left_half):
        arr[merged_index] = left_half[left_index] # Place the current element from the left_half into the merged array
        left_index += 1 # Move to the next element in left_half
        merged_index += 1 # Move to the next position in the merged array
    
    while right_index < len(right_half):
        arr[merged_index] = right_half[right_index]
        right_index += 1 # Move to the next element in right_half
        merged_index += 1 # Move to the next position in the merged array
    

# Example Usages
arr = [2, 5, 7, 1, 22, 45, 23, 76, 3, 24, 99, 61]
merge_sort(arr)
print("Sorted Arr: ", arr)
    
    