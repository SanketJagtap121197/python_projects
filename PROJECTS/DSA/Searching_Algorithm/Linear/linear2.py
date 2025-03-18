def linear_search(arr, target):
    """
    Perform a linear search on the given list to find all occurrences of the target element.
    :param arr: List of elements
    :param target: Element to search for
    :return: List of indices where the element is found, else an empty list
    """
    indices = []  # Initialize an empty list to store found indices
    for index, element in enumerate(arr):  # Loop through each element in the list with its index
        if element == target:  # Check if the current element matches the target
            indices.append(index)  # Store the index if the element is found
    return indices  # Return the list of indices (empty if not found)

# Example usage
if __name__ == "__main__":
    try:
        arr = list(map(int, input("Enter the elements separated by space: ").split()))  # Take input as space-separated numbers and convert to list
        target = int(input("Enter the number to search: "))  # Ask the user for the target number to search
        
        result = linear_search(arr, target)  # Call the linear_search function
        
        if result:  # If the result list is not empty
            print(f"Element found at indices: {result}")  # Print all found indices
        else:
            print("Element not found in the list")  # Print a message if the element is not found
    except ValueError:
        print("Invalid input! Please enter integers only.")  # Handle non-integer inputs
