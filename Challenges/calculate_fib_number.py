# Write some code to calculate the 123rd Fibonacci Number

def fib(n):
    if n < 2:
        return("Please go higher than 1 to begin the fib calculation")
    return fib(n-2) + fib(n-1)
        
print(input(n))