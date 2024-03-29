# Quick Sort Algorithm (Often used)

# Divide and Conquer Algorithm using Pivots and partitioning into two sub arrays

# Best Time Complexity: O(n log (n)) - when dividing into equal halves
# Average Time Complexity: O(n log (n)) 
# Worst Time Complexity: O(O n^2) - when a pivot is chosen poorly and creates unbalanced subarrays

# Space Complexity: O(n log (n)) - quite efficient for memory usage because of the recursion stack

def quick_sort(arr):
    # Base case: return array if 1 or less elements are inside the array
    if len(arr) <= 1:
        return arr 
    
    # Choose a pivot
    pivot = arr[len(arr) // 2] # Pick the middle element of the array. Use Square brackets to access the elements in the array using their index positions
        # Please note that using the integer division above can cause issues with picking an unbalanced pivot because integer division rounds down to zero rather than a decimal
    
    # Partition the array into three sub arrays
    # x is the shorthand way of saying element
    left = [x for x in arr if x < pivot] # create a list called left that takes array elements less than the pivot element
    middle = [x for x in arr if x == pivot] # create a list called middle that takes array elements that equal the pivot element 
    right = [x for x in arr if x > pivot] # create a list called right that takes array elements greater than the pivot element
    
    return quick_sort(left) + middle + quick_sort(right) # recursively calls the function for each side of the array and returns it concatenated    
        
# Example usage:
unsorted_array = [9, 4, 3, 5, 7, 3, 1, 2, 5, 7, 8, 9, 0, 6, 4, 3, 1]        
sorted_array = quick_sort(unsorted_array)
print(f'The Sorted Array is: {sorted_array}')
        
# Ways to improve this algorithm: 
    # 1. Randomized pivot
    # 2. Choose the middle of three randomly selected elements as the pivot
    # 3. Median of Medians: Select groups of elements, find their median and then choose the median of the medians as the pivot
    # 4. Hybrid Approach: Inside Quicksort switch to Insertion Sort for smaller subarrays
    
    