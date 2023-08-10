# Binary Search Algorithm (Integers)

# Time complexity: O(log n)

# Divide and conquer style algorithm on integers
# Efficient for ordered number lists

def binary_search(arr, target):
    low, high = 0, len(arr) -1

    while low <= high:
        # calculate the middle element
        mid = low + (high-low) // 2 # floor division operator divides by 2 and rounds down
        
        if arr[mid] == target:
            return mid
        elif arr[mid < target]:
            low = mid + 1
        else: 
            high = mid - 1
        
    return -1

list = [2, 4, 6, 9, 13, 17, 19, 21, 22, 23, 55, 80, 100, 140, 150, 173, 189, 200]

target = 173

result = binary_search(list, target)

if result != -1:
    print(f'Array item {target} found at index {result}.')
else:
    print(f'Array item {target} not found in the array.')
