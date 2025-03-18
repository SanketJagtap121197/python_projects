# Binary Search Implementation (Iterative and Recursive) in Python

# Function for iterative binary search
def binary_search_iterative(arr, target):
    left, right = 0, len(arr) - 1  # Define the search boundaries
    
    while left <= right:  # Continue while search space is valid
        mid = (left + right) // 2  # Find the middle index
        
        if arr[mid] == target:  # If target is found, return index
            return mid
        elif arr[mid] < target:  # If target is greater, search in the right half
            left = mid + 1
        else:  # If target is smaller, search in the left half
            right = mid - 1
    
    return -1  # Target not found

# Function for recursive binary search
def binary_search_recursive(arr, left, right, target):
    if left > right:  # Base case: if search space is invalid
        return -1
    
    mid = (left + right) // 2  # Find the middle index
    
    if arr[mid] == target:  # If target is found, return index
        return mid
    elif arr[mid] < target:  # If target is greater, search in the right half
        return binary_search_recursive(arr, mid + 1, right, target)
    else:  # If target is smaller, search in the left half
        return binary_search_recursive(arr, left, mid - 1, target)

# Taking user input for the sorted array
arr = list(map(int, input("Enter sorted numbers separated by space: ").split()))
target = int(input("Enter the number to search: "))

# Calling iterative binary search
result_iterative = binary_search_iterative(arr, target)
print("Iterative Binary Search Result:", "Found at index" if result_iterative != -1 else "Not found", result_iterative)

# Calling recursive binary search
result_recursive = binary_search_recursive(arr, 0, len(arr) - 1, target)
print("Recursive Binary Search Result:", "Found at index" if result_recursive != -1 else "Not found", result_recursive)
