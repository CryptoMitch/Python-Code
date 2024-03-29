# Bubble Sort Algorithm (Educational Purposes Only)

# steps through the list, compares adjacent elements, and swaps them if they're in the wrong order.

# Time Complexity: O(n^2) - "Quadratic"
# Space Complexity: O(1)
# Really slow and not useful for production environments

def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
arr = [63, 4, 33, 56, 86, 334, 754, 32, 2, 3, 54, 2, 23]

bubble_sort(arr)
print("Sorted Array Results: ", arr)