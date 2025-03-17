def create_array():
    arr = []
    num = int(input("Enter the number of elements in array: "))
    for i in range(num):
        element = int(input(f"Enter element {i+1}: "))
        arr.append(element)
    return arr

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
    print("Array elements:", end=" ")
    for i in arr:
        print(i, end=" ")
    print()

def reverse_array(arr):
    return arr[::-1]

def find_max_min(arr):
    return max(arr), min(arr)

# Main function
def main():
    arr = create_array()
    while True:
        print("\nOperations:")
        print("1. Insert")
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
            continue  # Go back to menu without executing below code

        if choice == 1:
            arr = insert_element(arr)
            print("Updated Array:", arr)
        elif choice == 2:
            arr = delete_element(arr)
            print("Updated Array:", arr)
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

