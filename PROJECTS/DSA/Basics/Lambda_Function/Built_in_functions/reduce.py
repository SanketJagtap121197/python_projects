# reduce(function, iterable)

#reduce() (from functools module) 
# It is used to apply a function to all elements in the iterable. This function receives two arguments and returns a single value.

from functools import reduce
sum_numbers = reduce(lambda x, y: x + y, [1, 2, 3, 4])
print(sum_numbers)  # Output: 10
