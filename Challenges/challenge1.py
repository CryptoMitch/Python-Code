# Question: 
# Write a program which will find all such numbers which
# are divisible by 7 but are not a multiple of 5, 
# between 2000 and 3200 (both included). 
# The numbers obtained should be printed in a 
# comma-separated sequence on a single line.

# Skills Demonstrated: 
#   range() function 
#   join() function - joins the strings together
#   map() function - convert numbers into strings
# Docs: https://www.w3schools.com/python/ref_func_range.asp


# My Solution

# Look for numbers in range starting with 2000 and ending in 3200
# Look for numbers whose remainder is 0 when divided by 7 but not by 5.
x = [n for n in range(2000, 3201) if n % 7 == 0 and n % 5 != 0]

# Print the result of this
    # Create results variable to hold the joined results
# Add a comma after each number

result = ', '.join(map(str, x))
print(result)

#The Answer Provided by the Tutorial

l=[]
for i in range(2000, 3201):
    if (i%7==0) and (i%5!=0):
        l.append(str(i))

print(','.join(l))


#How my answer differed and what I could do to improve it?