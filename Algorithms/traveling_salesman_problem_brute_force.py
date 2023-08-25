# Traveling Salesman Problem (TSP) Brute Force: 
# Time Complexity: O(n!)

# Do not use in production code as it has factorial time complexity which is one of the least efficient.

# For example, with just 10 cities, you'd need to perform 3,628,800 operations. 
# With 20 cities, you'd need to perform 2,432,902,008,176,640,000 operations, which is a staggering number.

# The Traveling Salesman Problem is a classic optimization problem. 
# It involves finding the shortest possible route that visits a set of cities 
# and returns to the starting city. The brute-force solution involves checking 
# all possible permutations of cities to find the shortest route.

# n is the number of cities. The algorithm checks all possible permutations of cities

import itertools # tools for working with iterators, combinations, and permutations.















# Two Arrays of Cities to Test Number of Operations

australian_cities = [
    "Sydney", "Melbourne", "Brisbane", "Perth", 
    "Adelaide", "Gold Coast", "Canberra", 
    "Newcastle", "Hobart", "Darwin"
]

asian_cities = [
    "Tokyo", "Seoul", "Shanghai", "Beijing", "Bangkok",
    "Mumbai", "Singapore", "Kuala Lumpur", "Jakarta", "Manila",
    "Delhi", "Taipei", "Hanoi", "Ho Chi Minh City", "Osaka",
    "Kyoto", "Hong Kong", "Dubai", "Kolkata", "Karachi"
]