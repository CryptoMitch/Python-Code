# Merge Sort Algorithm

# Summary: Divide-and-conquer sorting algorithm. Break down lists into sublists and merge those lists back in

# Time Complexity: O(n log n)

# Space Complexity: O(n) 


#Steps 
    # Divide
    # Conquer
    # Merge


def merge_sort(arr):
    # if the length of the array is greater than 1
    if len(arr) > 1:
        # Find the middle
        mid = len(arr) // 2
        # Divide the array into two lists
        left_half = arr[:mid] # Use slice notation to create left sublist
        right_half = arr[mid:] # Use slice notation to create right sublist
        