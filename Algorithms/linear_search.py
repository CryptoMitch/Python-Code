# Linear Search Algorithm

# Time complexity: O(n)

# Sequentially checks each element in a list until a match is found 
# or the entire list has been searched.

import time

# The Algorithm
def linear_search(arr, target):
    index = 0
    while index < len(arr):
        if arr[index] == target:
            return index
        index += 1
    return -1 

# The list + target
my_list = [1, 5, 8, 9, 12, 15, 18, 23, 55, 74, 81, 90, 99, 111, 154, 186, 200]
target = 99

# Track the time taken
start_time = time.time() # Store start time in a variable
# Execute the function
result = linear_search(my_list, 99) 
end_time = time.time() # Store end time in a variable

# Calculate the elapsed time
elapsed_time = end_time - start_time
print(f'Linear search took {elapsed_time: .6f} seconds')


print(f'Index location: {result}')