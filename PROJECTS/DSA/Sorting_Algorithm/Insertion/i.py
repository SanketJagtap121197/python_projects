# Function to perform insertion sort
def insertion_sort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]  # Select the current element to be placed correctly
        j = i - 1  # Start comparing with the previous elements
        
        # Move elements that are greater than key one position ahead
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key  # Place the key at its correct position
    
    return arr  # Return sorted array

def main() :

    # Taking user input
    nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
    print("Initial array:", nums)

    # Sorting the list
    sorted_nums = insertion_sort(nums)

    # Displaying sorted numbers
    print("Sorted array:", sorted_nums)

if __name__ == "__main__" :
    main()
