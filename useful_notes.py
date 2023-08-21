# List of Useful Python Syntax

# ___________________________________________________________________ #

##### Class #####

class myClass: # Class constructor
    def __init__(self, value):
       # Constructor method
        self.value = value
        
    def update_value(self, new_value):
        self.value = new_value
        
    def get_value(self):
        return self.value 

# Create an instance of the class
my_instance = myClass(42)

# Access the attribute of the instance
print(f"Instance Value:  {my_instance.value}")  # Output: 42        
        
# ___________________________________________________________________ #        
        
##### Data Structures #####        

my_list = [] # List 
my_list.append()
    # Good for odered collections of items and performing operations like 
    # Example: Storing user names, to-do list items, log entries.


# Dictionary
my_dict = {'a':1, 'b':2, 'c':3, 'd':4} 
for key, value in my_dict.items()
    # Good for storing key value pairs, in an unordered way, enabling fast lookup.
    # Bad when you don't need associated values with keys or if you need to maintain specifc order
    # Sytax, curly brackets and key value pairs
    # Good Example: Storing user data with usernames as keys, mapping countries to their capitals.
    # Bad Usage: Inefficient for storing a simple list of values without associated keys
    
# Ordered Dictionary
from collections import OrderedDict

my_ordered_dict = OrderedDict()
    # Good when you need to order your key value pairs

# Tuples
my_tuple = (1, 2, 3)
# Similiar to a list but is immutable, useful for unchangeble sequences or data
# Good Example: Storing latitude and longitude coordinates.
# Bad Usage: Storing a dynamic list of shopping cart items where quantities change

# Sets
my_set = {1, 2, 3, 4}
my_set.add(5) # Adding an element to the set
    # Good for storing a collection of unique elements and fast membership testing
    # Bad for maintaining items specific order, or accessing items by index
    # Syntax, curly brackets and only values
    # Example: Keeping track of users who have liked a post, storing unique email addresses.
    # Bad usage: Storing a sequence of items where order matters, like a playlist

# ___________________________________________________________________ #

#### Loops ####

# For Loop

for i in range(5): # looping from 0 - 4
    print(i)
    # Use 'for' loops to iterate through sequences like lists, tuples, and strings.


# While loop
count = 0
while count < 5:
    print(count)
    count += 1
    # Use 'while' loops when you need to repeatedly execute a block of code as long as a condition is met.
    # Bad usage: When you know the loop will never be entered or will run indefinitely

# If Elif Else loop
x = 10
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")
    

# Nested loops

for i in range(5): # looping from 0 - 4
    for j in range(3):
        print(f"({i}, {j})")
    # Nested loops are good for looping inside other loops on multidimensional data or combinations
    # Bad usage:When you have a large number of nested loops, leading to inefficient code
    # How to fix: Optimise the algorithm
    
    
# Break and Continue Statements
for i in range(10):
    if i == 5:
        break
    if i % 2 == 0:
        continue # Skip even numbers
    print(i)
# The 'break' statement immediately exits the loop.
# The 'continue' statement skips the current iteration and moves to the next one.    
# Bad usage: Breaking out of a loop prematurely without a clear reason or skipping steps inappropriately
   
# Enumerate loop

fruits = []
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

# Good for getting both index and value in a sequence or iterating through elements while keeping track of their positions
# Bad when you only need one index or value or if you don't need the position values
# Bad usage: When you only need to iterate through the sequence without tracking indices

# ___________________________________________________________________ #


##### Built in Functions and Libraries #####

sorted()
list.sort()
list.index()
str.find()


# Binary Search Functions
import bisect


# Mathematical Operations
import math 

# Regular expressions

import re


##### Libraries #####

import NumPy: # For numerical and scientific computing.
import Pandas: # For data manipulation and analysis.
import SciPy: # For advanced scientific and technical computations.
import NetworkX: # For graph algorithms and analysis.
import sklearn: # For machine learning algorithms.
