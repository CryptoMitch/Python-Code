# Slice Notation Notes

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#Basic Slicing:

arr[start:stop]:        # Returns elements from index start to stop - 1.
arr[:stop]:             # Returns elements from the beginning up to index stop - 1.
arr[start:]:            # Returns elements from index start to the end of the sequence.

# Negative Indices:
                        # You can use negative indices to count positions from the end of the sequence. -1 refers to the last element.
arr[-1]:                # Returns the last element.
arr[:-1]:               # Returns all elements except the last one.

# Slicing with Step:

arr[start:stop:step]:   # Returns elements from index start to stop - 1 with a step size of step.
arr[::2]:               # Returns every second element.
arr[::-1]:              # Reverses the sequence.

# String Slicing: Slicing works similarly for strings.

"Hello"[1:4]            # returns "ell".
"Hello"[::-1]           # returns "olleH".

# Using Slice in Assignments:

                        # You can also use slices to modify parts of a sequence.
arr[1:4] = [10, 20, 30] # replaces elements from index 1 to 3 with the new values.

# Default Values:

# If you omit start, it's assumed to be 0.
# If you omit stop, it's assumed to be the end of the sequence.
# If you omit step, it's assumed to be 1.




# TDD Tests for Slice Notation

def test_slice_notation():
    # Test for Basic Slicing
    arr1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert arr1[1:4] == [1, 2, 3]
    assert arr1[3:6] == [3, 4, 5,]
    assert arr1[3:] == [4, 5, 6, 7, 8, 9]
    
    # Test case 2: Negative indices
    arr2 = [10, 20, 30, 40, 50]
    assert arr2[-1] == 50
    assert arr2[:-1] == [10, 20, 30, 40]
    
    # Test case 3: Slicing with step
    arr3 = [100, 200, 300, 400, 500]
    assert arr3[::2] == [100, 300, 500]
    assert arr3[::-1] == [500, 400, 300, 200, 100]
    
    # Test case 4: String slicing
    word = "Happy"
    assert word[1:4] == "app"
    assert word[::-1] == "yppaH"

    # Test case 5: Using slice in assignments
    arr4 = [0, 1, 2, 3, 4]
    arr4[1:4] = [10, 20, 30]
    assert arr4 == [0, 10, 20, 30, 4]
    
    print("All slice notation test cases passed!")
    
test_slice_notation()