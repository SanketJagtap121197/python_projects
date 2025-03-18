#Taking user input for the numbers to find odd and even numbers
numbers = list(map(int, input("Enter the numbers seperated by spaces: ").split()))

# Using filter and lambda function to find even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# syntax of filter() ---> filter(function, iterable)  VERY IMPORTANT

# Using filter and lambda function to find odd numbers
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))

# Displaying the even and odd numbers
print(f'Even numbers: {even_numbers}')
# we can also use ---> print("Even Numbers:", even_numbers) instead of above line
print(f'Odd numbers: {odd_numbers}')

