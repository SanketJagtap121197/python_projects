
def selection_sort (arr) :
    n = len(arr)
    for i in range(n) :
        min_idx = i
        for j in range(i+1, n) :
            if arr[j] < arr[min_idx] :
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def main () :

    user_input = input("Enter the list of numbers seperated by spaces : ")

    '''
    numbers = list(map(int, elements.split()))  # Convert input strings to integers

    # Sorting the array using Selection Sort
    selection_sort(numbers)

    # Display the sorted array
    print("Sorted array:", numbers)
    '''
    #Instead of above code we can write the below code

    arr = list(map(int, user_input.split()))
    print("Original List : ", arr )

    selection_sort(arr)

    print("Sorted List : ", arr)

if __name__ == "__main__" :
    main()

