# Traveling Salesman Problem (TSP) Brute Force: 
# Time Complexity: O(n!)

# The Traveling Salesman Problem is a classic optimization problem. 
# It involves finding the shortest possible route that visits a set of cities and returns to the starting city. 
# The brute-force solution involves checking all possible permutations of cities to find the shortest route.

# Do not use in production code as it has factorial time complexity which is one of the least efficient.

# For example, with just 10 cities, you'd need to perform 3,628,800 operations. 
# With 20 cities, you'd need to perform 2,432,902,008,176,640,000 operations, which is a staggering number.

import itertools # tools for working with iterators, combinations, and permutations.
import math 

def distance(city1, city2):
    return 0

def total_distance(path): # calculates the total distance of a given path
    total = 0 # encapsulate the variable inside the function to localise the scope
    for i in range(len(path) - 1):
        total += distance(path[i], path[i + 1]) # calculates the distance between the current city and the next city
    total += distance(path[-1], path[0]) # calculates the distance required to return to the starting city then add to total
    return total # return the accumulated total distance

# Define the dictionary of Australian cities
australian_cities = {
    "Sydney":(-33.8688, 151.2093), 
    "Melbourne": (-37.8136, 144.9631), 
    "Brisbane": (-27.4698, 153.0251), 
    "Perth" : (-31.9505, 115.8605), 
    "Adelaide": (-34.9285, 138.6007), 
    "Gold Coast": (-28.0167, 153.4000), 
    "Canberra": (-35.2809, 149.1300), 
    "Newcastle": (-32.9272, 151.7817), 
    "Hobart": (-42.8821, 147.3272), 
    "Darwin": (-12.4628, 130.8417)
}
        
def brute_force_tsp(australian_cities):
    shortest_path = None
    shortest_distance = float('inf') # initialise local variable with no upper bound for shortest distance
    
    for path in itertools.permutations(australian_cities):   # Call permutations function from itertools module to generate all possible permutations
        d = total_distance(path) # Calculate the total distance for the current path
        if d < shortest_distance: # check if current path total distance is shorter than shortest distance found so far
            shortest_distance = d # update the new shortest distance
            shortest_path = path
            
    return shortest_path, shortest_distance

# Tuple unpacking to be able to capture and display the results
best_path, best_distance = brute_force_tsp(australian_cities.values())


formatted_path = ' -> '.join(city for city in australian_cities.keys())

print("Shortest path:", formatted_path)
print("Shortest distance: ", best_distance)


# Two Arrays of Cities to Test Number of Operations

asian_cities = {
    "Tokyo": (35.6895, 139.6917),
    "Seoul": (37.5665, 126.9780),
    "Shanghai": (31.2304, 121.4737),
    "Beijing": (39.9042, 116.4074),
    "Bangkok": (13.7563, 100.5018),
    "Mumbai": (19.0760, 72.8777),
    "Singapore": (1.3521, 103.8198),
    "Kuala Lumpur": (3.1390, 101.6869),
    "Jakarta": (-6.2088, 106.8456),
    "Manila": (14.5995, 120.9842),
    "Delhi": (28.6139, 77.2090),
    "Taipei": (25.0320, 121.5654),
    "Hanoi": (21.0285, 105.8542),
    "Ho Chi Minh City": (10.8231, 106.6297),
    "Osaka": (34.6937, 135.5023),
    "Kyoto": (35.0116, 135.7681),
    "Hong Kong": (22.3193, 114.1694),
    "Dubai": (25.276987, 55.296249),
    "Kolkata": (22.5726, 88.3639),
    "Karachi": (24.8607, 67.0011)
}