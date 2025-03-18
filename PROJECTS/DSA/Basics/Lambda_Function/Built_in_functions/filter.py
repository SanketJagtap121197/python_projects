# filter(function, iterable)

'''
function: A function that returns True or False
iterable: The sequence (list, tuple, etc.) to filter
'''

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(even_numbers)  # Output: [2, 4, 6, 8, 10]
