# Breadth First Search (BFS) Algorithm
# Summary: Traverse or search through data structures like graphs or trees level by level.
# Time Complexity: 
# Space Complexity:

# Import module to support adding and subtracting elements from both ends
from collections import deque

def bfs_algorithm(graph, start): # start will receive the start_node argument at runtime
    traversed = set() # To keep track of the traversed nodes
    queue = deque([start]) # Initialise the queue with the starting node which is passed in by start_node




# Explore neighbours



# Move to the next level of the queue


    # Do this until the queue is empty





# Implement Graph that is the Adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
}

# Start at the root(AKA arbitrary or inital) node in a graph
start_node = 'A'
print('Breadth-First Search: ')
bfs_algorithm(graph, start_node) # Calls the implementation of the BFS algorithm