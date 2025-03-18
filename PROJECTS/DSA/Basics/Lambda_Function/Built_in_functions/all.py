# all(iterable)

# It is a built-in function in Python that returns True if all elements of the iterable are True. If the iterable is empty, it returns True.

nums = [1, 2, 3, 4]
print(all(map(lambda x: x > 0, nums)))  # Output: True
