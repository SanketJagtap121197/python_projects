squares = [x**2 for x in range(5)]
print(squares)

# Output:
# [0, 1, 4, 9, 16]
# List comprehension is a concise way to create lists.
# The syntax is [expression for item in iterable].
# The expression is the operation performed on the item.
# The item is the variable representing each element in the iterable.
# The iterable is the sequence of elements that will be iterated.
# The list comprehension will return a list.
# In this example, the list comprehension will return a list of squares.
# The range() function will return a sequence of numbers from 0 to 4.
# The for loop will iterate through each number in the range.
# The expression x**2 will square each number.
# The squared number will be added to the list.
# The list will contain the squares of the numbers from 0 to 4.
# The list will be [0, 1, 4, 9, 16].