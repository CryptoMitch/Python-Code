# Haversine Formula
# ChatGPT assisted significantly in this section
# This is a curiousity project

# The Haversine formula is used to calculate the distance 
# between two points on the surface of a sphere, 
# given their latitude and longitude coordinates.


# ChatGPT helped me understand this mathematical formula 
# for my deep dive into the Traveling Salesman Problem

    # Haversine Formula 
    
    # a = sin²(Δlat / 2) + cos(lat1) * cos(lat2) * sin²(Δlong / 2)
    # c = 2 * atan2(√a, √(1-a))
    # distance = R * c
    
    # Where:
        # lat1 and long1 are the latitude and longitude of the first point.
        # lat2 and long2 are the latitude and longitude of the second point.
        # Δlat and Δlong are the differences between the latitudes and longitudes of the two points.
        # R is the Earth's radius (mean radius = 6,371 km).
        # sin, cos, and atan2 are trigonometric functions.
        
# Python Implementation of the Haversine Formula

import math # This code uses radians(), sin(), cos(), and atan2().

def haversine_distance(coord1, coord2):
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    
    R = 6371.0 # Earths radius in kilometers
    
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)

    a = math.sin(dlat / 2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distance = R * c
    return distance

coord1 = (-33.8688, 151.2093)  # Sydney
coord2 = (-37.8136, 144.9631)  # Melbourne
distance = haversine_distance(coord1, coord2)
print("Distance:", distance, "km")