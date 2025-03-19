# Merge Sort Implementation with User Input

def merge_sort(arr):
    # Base case: If the array has 1 or 0 elements, it's already sorted
    if len(arr) <= 1:
        return arr
    
    # Find the middle index of the array
    mid = len(arr) // 2
    
    '''
    This line of code is used to find the middle index of the array in order to split it into two halves.

    Breakdown:
    len(arr): Calculates the total number of elements in the array.
    // 2: Performs integer division, ensuring that mid is always an integer.
    
    Why is this needed? 2 reasons
    
    1. Splitting the array
    Merge Sort follows the divide and conquer approach.
    The array is divided into two smaller sub-arrays at index mid.
    
    2. Recursive sorting
    The left half is arr[:mid] (from index 0 to mid-1).
    The right half is arr[mid:] (from index mid to the end).
    These halves are then sorted recursively.

    Example:
    If arr = [7, 3, 8, 5, 2],
    len(arr) = 5
    mid = 5 // 2 = 2
    Left half: arr[:2] = [7, 3]
    Right half: arr[2:] = [8, 5, 2]
    This ensures that Merge Sort correctly breaks down the array into smaller parts before merging them back in sorted order.
    '''
    # Recursively split and sort the left and right halves
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    '''
    Explanation
    arr[:mid] → This creates a slice of the array from the beginning (0) to the middle index (mid).
    merge_sort(arr[:mid]) → This recursively calls merge_sort on the left half of the array.
    Why is this used?
    Splitting the array → Merge Sort follows a divide and conquer approach. This helps in dividing the array into smaller parts.
    Recursive sorting → We keep calling merge_sort() until each sub-array has only one element.
    Merging back later → After sorting both halves, they will be merged back in sorted order.
    '''
    
    # Merge the sorted halves and return the sorted array
    return merge(left_half, right_half)

def merge(left, right):
    sorted_arr = []  # Initialize an empty list to store sorted elements
    i = j = 0  # Pointers for left and right lists
    
    # Compare elements from both lists and add the smaller one
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1
    
    # Add remaining elements from left and right lists, if any
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])
    
    return sorted_arr

# Take user input
user_input = input("Enter numbers separated by spaces: ")

# Convert input string into a list of integers
arr = list(map(int, user_input.split()))   #Instead of arr we can use any variable name like e.g. numbers but we have to replace arr with numbers in the next line and also in the next to next line.

# Sort the array using merge sort
sorted_array = merge_sort(arr)

# Display the sorted array
print("Sorted array:", sorted_array)
