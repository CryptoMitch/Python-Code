# A challenge I set for myself
# Select even numbers from the list, provide those numbers, square and provide those numbers, provide numbers divisible by 8.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
squared_even_numbers = [x**2 for x in numbers if x % 2 == 0]
squared_even_numbers_divisible_by_8 = [x for x in numbers if x % 8 == 0]

print("Original numbers:", numbers)
print("Squared even numbers:", squared_even_numbers)
print("Numbers divisible by 8:", squared_even_numbers_divisible_by_8)