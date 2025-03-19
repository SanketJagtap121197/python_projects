# Quick Sort implementation in Python with user input (Divide and Conquer algorithm)

def quick_sort(arr):  # Function to perform Quick Sort
    if len(arr) <= 1:  # Base case: If the list has 0 or 1 element, it is already sorted
        return arr
    else:
        pivot = arr[0]  # Choosing the first element as the pivot
        '''
        The first element of the array is chosen as the pivot.
        The pivot helps in partitioning the array into two parts
        '''
        left = [x for x in arr[1:] if x <= pivot]  # Elements less than or equal to pivot
        right = [x for x in arr[1:] if x > pivot]  # Elements greater than pivot
        '''
        The left list contains all elements less than or equal to the pivot.
        The right list contains all elements greater than the pivot.
        This step ensures that elements smaller than the pivot go to one (left of pivot element) side, and larger elements go to the other(right of pivot element) side.
        '''
        return quick_sort(left) + [pivot] + quick_sort(right)  # Recursively sorting left and right parts
        '''
        This recursively calls the quick_sort function on the left subarray (which contains elements ≤ pivot).
        It continues dividing and sorting the left part until all elements are in order
        Then, it appends the pivot element to the sorted left part
        Finally, it recursively calls the quick_sort function on the right subarray (which contains elements > pivot).
        It continues dividing and sorting the right part until all elements are in order
        The sorted left part, pivot element, and sorted right part are concatenated and returned as the sorted array
        '''
        
# Taking user input as a space-separated list of numbers
user_input = input("Enter numbers separated by spaces: ")
numbers = list(map(int, user_input.split()))  # Converting input string to a list of integers

sorted_numbers = quick_sort(numbers)  # Calling Quick Sort function
print("Sorted numbers:", sorted_numbers)  # Displaying the sorted list
