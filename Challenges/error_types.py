# This is a place for me to test and store common error types in python

# SyntaxError: Missing closing parenthesis
print("Hello, world!"

# IndentationError: Inconsistent indentation
for i in range(5):
print(i)

# NameError: Using an undefined variable
print(undefined_variable)

# TypeError: Adding incompatible types
result = "42" + 5

# ValueError: Converting an invalid string to int
number = int("abc")

# ZeroDivisionError: Division by zero
result = 10 / 0

# IndexError: Accessing an index that doesn't exist
my_list = [1, 2, 3]
print(my_list[5])

# KeyError: Accessing a non-existent key in a dictionary
my_dict = {'a': 1, 'b': 2}
print(my_dict['c'])

# FileNotFoundError: Trying to open a non-existent file
with open("nonexistent_file.txt", "r") as file:
    content = file.read()

# ImportError: Trying to import a non-existent module
import non_existent_module

# AttributeError: Accessing a non-existent attribute
my_string = "Hello"
print(my_string.uppercase())

# AssertionError: Failing an assert statement
assert 5 > 10, "5 is not greater than 10"

# RuntimeError: Raising a custom runtime error
raise RuntimeError("This is a custom runtime error")
