# Sliding Windown Algorithmic Pattern

# Time Complexity: O(n) or O(n+m) n = size of input, m = size of the sliding window
# Space Complexity: O(1)

def max_subarray_sum(arr, k):   #k = size of sliding window
    max_sum = float("-inf") # Initialise max sum variable to negative infinity to ensure it works even if all the numbers are negative
    window_sum = sum(arr[:k]) # Initial sum of the first subarray (first window)
    
    for i in range(k, len(arr)): #intialise a loop that goes thow the array to the end
        window_sum += arr[i] - arr[i - k] # Slide the window. arr[i] = current element that enters the window
        
        max_sum = max(max_sum, window_sum) #    
    
    return max_sum