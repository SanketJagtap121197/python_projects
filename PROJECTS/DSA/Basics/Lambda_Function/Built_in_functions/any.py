# any(iterable) 

# It is a built-in function in Python that returns True if any element of the iterable is True. If the iterable is empty, it returns False.

nums = [0, 1, 0, 0]
print(any(map(lambda x: x > 0, nums)))  # Output: True
