# Write some code to calculate the 123rd Fibonacci Number

def fib(n):
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)

user_input = int(input("Which Fibonacci Number would you like to calculate? "))
result = fib(user_input)
print(f"The {user_input}th Fibonacci number is: {result}")