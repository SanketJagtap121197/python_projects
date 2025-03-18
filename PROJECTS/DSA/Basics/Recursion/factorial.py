def factorial(n) :
    """
    Recursively calculates the factorial of a number.
    
    :param n: The number to calculate factorial for.
    :return: The factorial of n.
    """

    if n == 0 or n == 1 :
        return 1
    else :
        return n * factorial(n-1)
    
    # Run the factorial function
if __name__ == "__main__" :
    num = int(input("Enter a number to calculate factorial for : "))
    if num < 0 :
        print("Factorial is not defined for negative numbers, please enter a positive number.")
    else :
        print(f'Factorial of {num} is {factorial(num)}')