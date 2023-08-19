# Breadth First Search (BFS) Algorithm
# Summary: Traverse or search through data structures like graphs or trees level by level.
# Time Complexity: O(V + E) where V is the number of vertices and E is the number of edges.
# Space Complexity: O(V) where V is the number of vertices.

# Import module to support adding and subtracting elements from both ends
from collections import deque

def bfs_algorithm(graph, start):    # start will receive the start_node argument at runtime
    traversed = set()               # To keep track of the traversed nodes
    queue = deque([start])          # Initialise the queue with the starting node which is passed in by start_node

    while queue:                    # continue running while there are nodes in the queue
        node = queue.popleft()      # Dequeue the front node. Select the next node to be processed from the queue
        if node not in traversed:   # Check if current node is in the set to avoid multiple traverses
            traversed.add(node)     # Adding the node to the set indicates that it has been traversed.
            queue.extend(neighbor for neighbor in graph[node] if neighbor not in traversed)


# Implement Graph that is the Adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': [],
}

# Start at the root(AKA arbitrary or inital) node in a graph
start_node = 'A'
print('Breadth-First Search: ')
bfs_algorithm(graph, start_node) # Calls the implementation of the BFS algorithm