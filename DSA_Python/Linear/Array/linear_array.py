def create_array():
    arr = []
    num = int(input("enter the number of elements in array : "))
    for i in range(num):
        element = int(input(f"enter element {i+1} : "))
        arr.append(element)
    return arr

'''
    # to try running created array
    arr = create_array()
    print("final array : ", arr)
'''
def insert_element(arr):
    index = int(input("Enter the index to insert: "))
    value = int(input("Enter the value to insert: "))
    if 0 <= index <= len(arr):
        arr.insert(index, value)
    else:
        print("Invalid index!")
    return arr

def delete_element(arr):
    index = int(input("Enter the index to delete: "))
    if 0 <= index < len(arr):
        arr.pop(index)
    else:
        print("Invalid index!")
    return arr

def search_element(arr):
    value = int(input("Enter the value to search: "))
    if value in arr:
        print(f"Element found at index {arr.index(value)}")
    else:
        print("Element not found!")

def traverse_array(arr):
    print("Array elements:", end=" ")  # end=" " prevents a newline after each number, so elements are printed in a single row
    for i in arr:
        print(i, end=" ")
    print()

def reverse_array(arr):
    return arr[::-1]

def find_max_min(arr):
    return max(arr), min(arr)


# main function from where execution starts
def main():
    arr = create_array()
    while True:
        print(" Operations:")
        print("1.  Insert")
        print("2. Delete")
        print("3. Search")
        print("4. Traverse")
        print("5. Reverse")
        print("6. Max & Min")
        print("7. Exit")
    
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue  # Ask again

        if choice == 1:
            arr = insert_element(arr)
        elif choice == 2:
            arr = delete_element(arr)
        elif choice == 3:
            search_element(arr)
        elif choice == 4:
            traverse_array(arr)
        elif choice == 5:
            print("Reversed Array:", reverse_array(arr))
        elif choice == 6:
            max_val, min_val = find_max_min(arr)
            print(f"Maximum: {max_val}, Minimum: {min_val}")
        elif choice == 7:
            print("Exiting...")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()

# or just use main()
# why we used if __name__ == "__main__": Prevents main() from running when the file is imported into another script.
# allows reusability of functions in other programs.
