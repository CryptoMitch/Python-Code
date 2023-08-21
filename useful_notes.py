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
    # Good for odered collections of items and performing operations like 
my_list.append()

# Dictionary
my_dict = {} 
    # Good for storing key value pairs, in an unordered way, enabling fast lookup.
    # Bad when you don't need associated values with keys or if you need to maintain specifc order
    # Sytax, curly brackets and key value pairs

# Ordered Dictionary
from collections import OrderedDict

my_ordered_dict = OrderedDict()
    # Good when you need to order your key value pairs

# Tuples
my_tuple = (1, 2, 3)
# Similiar to a list but is immutable, useful for unchangeble sequences or data


# Sets
my_set = {1, 2, 3, 4}
    # Good for storing a collection of unique elements and fast membership testing
    # Bad for maintaining items specific order, or accessing items by index
    # Syntax, curly brackets and only values
my_set.add(5) # Adding an element to the set


# ___________________________________________________________________ #

#### Loops ####

# For Loop

for i in range(5): # looping from 0 - 4
    print(i)


# While loop
count = 0
while count < 5:
    print(count)
    count += 1


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


# Enumerate loop

fruits = []
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

# Good for getting both index and value in a sequence or iterating through elements while keeping track of their positions
# Bad when you only need one index or value or if you don't need the position values

# ___________________________________________________________________ #


# Set
