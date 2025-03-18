def linear_search(arr, target):
    """
    Perform a linear search on the given list to find the target element.
    :param arr: List of elements
    :param target: Element to search for
    :return: Index of the element if found, else -1
    """
    for index, element in enumerate(arr):  # Loop through each element in the list with its index
        if element == target:  # Check if the current element matches the target
            return index  # Return the index if the element is found
    return -1  # Return -1 if the element is not found

# Example usage
if __name__ == "__main__":
    arr = []  # Initialize an empty list to store user input elements
    n = int(input("Enter the number of elements: "))  # Ask the user for the number of elements
    for _ in range(n):  # Loop to get 'n' elements from the user
        arr.append(int(input("Enter element: ")))  # Append each entered element to the list
    
    target = int(input("Enter the number to search: "))  # Ask the user for the target number to search
    result = linear_search(arr, target)  # Call the linear_search function
    
    if result != -1:
        print(f"Element found at index {result}")  # Print the index if the element is found
    else:
        print("Element not found in the list")  # Print a message if the element is not found
