# Selection Sort Implementation in Python

def selection_sort(arr):
    n = len(arr)  # Get the length of the array
    for i in range(n):
        min_idx = i  # Assume the current index as the minimum
        for j in range(i + 1, n):  # Iterate through the unsorted part
            if arr[j] < arr[min_idx]:  # Find the smallest element
                min_idx = j  # Update the index of the smallest element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # Swap the smallest element with the first element of the unsorted part

# Taking user input
elements = input("Enter numbers separated by spaces: ")
numbers = list(map(int, elements.split()))  # Convert input strings to integers

# Sorting the array using Selection Sort
selection_sort(numbers)

# Display the sorted array
print("Sorted array:", numbers)
