from collections import deque  # Imported deque from collections for queue implementation

def display_menu():  # making a parameterless function
    """Functions to display menu options"""
    print("\nQueue operations")
    print("1. Add element (Enqueue) : ")
    print("2. Delete element (Dequeue) : ")
    print("3. Display Queue")
    print("4. Exit")

def main():
    queue = deque()   # Initializing an empty queue using deque
    # queue.append(element) allows enqueue (adding at the rear) in O(1) time.
    # queue.popleft() allows dequeue (removing from the front) in O(1) time, whereas a list would take O(n) time due to shifting elements.
        
    while True:
        display_menu()
        
        try:
            choice = int(input("Enter your choice (1 to 4) : "))
        except ValueError:
            print("Invalid input, enter only numbers")

        if choice == 1:   # Enqueue operation
            element = input("Enter the element to enqueue/add : ")   # Getting the element from the user
            queue.append(element)  # Adding the element to the queue
            print(f'{element} added to the queue')
            
        elif choice == 2:   # Dequeue operation
            if queue:  # Checking if the queue is not empty
                remove_element = queue.popleft()  # Removing the front element from the queue
                print(f'{remove_element} deleted from the queue')
            else:
                print("Empty queue, nothing to remove")
            
        elif choice == 3:   # Display queue operation
            if queue:  # Checking if the queue is not empty
                print("Current Queue : ", list(queue))   # Displaying queue elements
            else:
                print("Empty queue, nothing to display")


        elif choice == 4:
            print("Exiting...")
                
            break

        else:
            print("Invalid number, enter number between (1 to 4)")

if __name__ =="__main__":
    main() 
    #It ensures that the main() function only runs when the script is executed directly (explicitly).
    # Prevents unintended execution when the script is imported as a module in another (queue_script.py) automatic run (implicitly).
