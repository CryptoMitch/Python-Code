# Test Driven Development Approach to Solving the Problem

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        # TDD Solution

        # There are n kids with candies. 
        maxCandies = max(candies)
        result = [] #empty list to store the result
        
        # You are given an integer array candies, 
            # where each candies[i] represents the number of candies the ith kid has, 
        for i in range(len(candies)):
            # after giving the ith kid all the extraCandies, 
            if candies[i] + extraCandies >= maxCandies:
            # where result[i] is true if they will have the greatest number of candies among all the kids, 
                result.append(True)
            else:
                # or false otherwise.
                result.append(False)
        # Return a boolean array result of length n, 
        return result   


# Test cases 
def test_kids_with_candies():
    # Test case 1: 
    kids_existing_candies = [2, 5, 3, 4, 1]
    extra_candies = 3
    assert kids_with_extra_candies(kids_existing_candies, extra_candies) == [True, True, True, True, False]

    # Test case 2: 
    kids_with_candies = [4, 2, 1, 1, 2]
    extra_candies = 1
    assert kids_with_extra_candies(kids_existing_candies, extra_candies) == [True, False, False, False, False]

    # Test case 3:
    kids_with_candies = [12, 1, 12]
    extra_candies = 10
    assert kids_with_extra_candies(kids_existing_candies, extra_candies) == [True, False, True]

    print("All test cases passed!")

    test_kids_with_candies()