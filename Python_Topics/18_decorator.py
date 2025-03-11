def decorator_func(original_func):
    def wrapper():
        print("Executing before the function call")  # Before calling the original function
        original_func()  # Calling the original function
        print("Executing after the function call")  # After calling the original function
    return wrapper


# A decorator is a function that takes another function as input, modifies or enhances it, and returns the modified function

'''

decorator_func(original_func) → This is a decorator function that takes another function as an argument.
Inside it, there is a nested function wrapper():
Before calling the original function, it prints "Executing before the function call".
Calls the original_func() (which will be decorated).
After calling the original function, it prints "Executing after the function call".
The wrapper() function is returned, meaning the original function is replaced with this new function.

'''


'''
Applying the Decorator:

@decorator_func
def say_hello():
    print("Hello, World!")
What does @decorator_func do?
The @decorator_func is the same as writing:

say_hello = decorator_func(say_hello)

This means that say_hello is no longer the original function. Instead, it is now the wrapper() function from decorator_func

Calling say_hello()

say_hello()

Since say_hello is now actually wrapper(), it runs:

Prints "Executing before the function call"
Calls the original say_hello() function, which prints:
Hello, World!

Prints "Executing after the function call"

Final Output:
Executing before the function call
Hello, World!
Executing after the function call

'''