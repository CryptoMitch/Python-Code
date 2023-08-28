def euclidean_algorithm(a, b):
    while b: # loop continues while b is non-zero
        a, b = b, a % b
    return a

# Example usage
num1 = 36
num2 = 30
gcd = euclidean_algorithm(num1, num2)
print(f"The GCD of {num1} and {num2} is {gcd}")