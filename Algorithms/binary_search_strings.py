# Binary Search Algorithm (Strings)

# Time complexity: O(log n)

# Divide and conquer style algorithm on strings
# Efficient for ordered string lists

def binary_search(arr, target):
    low, high = 0, len(arr) -1

    while low <= high:
        mid = low + (high-low) // 2 # floor division operator divides by 2 and rounds down
        # Compare strings lexicographically
        comparison = arr[mid]
        
        if comparison == target:
            return mid
        elif comparison < target:
            low = mid + 1
        else: 
            high = mid - 1
        
    return -1

strings_list = ["Australia", "Brazil", "Canada", "China", "France", "Germany", "India", "Italy", "Japan", "Mexico", 
                   "Netherlands", "Russia", "Saudi Arabia", "South Korea", "Spain", "Sweden", "Switzerland", "Turkey", 
                   "United Kingdom", "United States"]

target = "Sweden"

result = binary_search(strings_list, target)

if result != -1:
    print(f'Array item {target} found at index {result}.')
else:
    print(f'Array item {target} not found in the array.')
