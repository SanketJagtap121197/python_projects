# Bubble Sort Implementation in Python with User Input

def bubble_sort (arr) :
    """
    Function to perform Bubble Sort on a given list.
    :param arr: List of numbers to be sorted
    """
    n = len(arr)

    for i in range (n) :
        swapped = False
        for j in range (0, n - i - 1) :
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped :
            break

def main() :

    user_input = input("Enter the list of numbers separated by spaces: ")

    arr = list(map(int, user_input.split()))

    print("Original List : ", arr)

    bubble_sort(arr)

    print("Sorted List : ", arr)

if __name__ == "__main__" : # the script will only execute when run directly (not when imported as a module in another script).
    main()