# Write some code to calculate the 123rd Fibonacci Number

def fib(n):
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)

user_input = int(input("Which Fibonacci Number would you like to calculate? "))
result = fib(user_input)
print(f"The {user_input}th Fibonacci number is: {result}")


# Test edge cases

def test_fibonacci_calculator():
    try:
        # Base cases
        assert fib(0) == 0
        assert fib(1) == 1
        
        # Small positive integers
        assert fib(2) == 1
        assert fib(3) == 2
        assert fib(4) == 3
        
        # Negative integers
        
        assert fib(-1) == -1
        assert fib(-2) == -2
        
        print("All tests passed!")
    except AssertionError as e:
        print("Assertion Error", e, "Tests failed")
    
test_fibonacci_calculator()