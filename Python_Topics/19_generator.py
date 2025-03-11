def my_generator():
    for i in range(3):  # Looping through values 0, 1, and 2
        yield i  # Yielding each value instead of returning

#Creating a Generator Object
gen = my_generator()

'''
    Calling my_generator() does not execute the function immediately.
    Instead, it creates a generator object (gen) that can be iterated over.
'''
# Fetching Values Using next()
print(next(gen))  # Output: 0

'''
    The first call to next(gen) executes my_generator() up to the first yield, which is 0.
    The generator pauses execution and remembers its state.
'''

print(next(gen))  # Output: 1

'''
    The second call resumes from where it left off and continues the loop.
    The next value 1 is yielded, and the function pauses again.
'''

print(next(gen))  # Output: 2
#The generator resumes, yields 2, and then pauses again.

'''
    Final Output

    0
    1
    2
'''

# What Happens If We Call next(gen) Again?

print(next(gen))  # Raises StopIteration


'''
    The generator has no more values left to yield.
    Calling next(gen) again raises a StopIteration error, indicating that the generator is exhausted
'''