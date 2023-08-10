# Binary Search Algorithm

# Time complexity: O(n)

Efficient search algorithm for ordered lists

def binary_search(arr, target):
    low, high = 0, len(arr) -1

    while low <= high:
        mid = low + (high-low) // 2
        
        if low (< target)
            += 1
        elif high (>= target)
            -= 1
        else mid == target
        return(mid)
    return -1

