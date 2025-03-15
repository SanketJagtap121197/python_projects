from collections import deque  # Importing deque from collections module for efficient double-ended queue operations

class Deque:
    def __init__(self):
        """Initialize an empty deque using collections.deque."""
        self.deque = deque()  # Create an empty deque
    
    def add_front(self, item):
        """Add an item to the front of the deque."""
        self.deque.appendleft(item)  # Use appendleft() to add item at the front
        print(f"Added {item} to the front.")  # Print confirmation message
    
    def add_rear(self, item):
        """Add an item to the rear of the deque."""
        self.deque.append(item)  # Use append() to add item at the rear
        print(f"Added {item} to the rear.")  # Print confirmation message
    
    def remove_front(self):
        """Remove and return the front item of the deque. If empty, display a message."""
        if self.is_empty():  # Check if deque is empty
            print("Deque is empty! Cannot remove from front.")  # Print error message
        else:
            removed = self.deque.popleft()  # Use popleft() to remove front item
            print(f"Removed {removed} from the front.")  # Print removed item
    
    def remove_rear(self):
        """Remove and return the rear item of the deque. If empty, display a message."""
        if self.is_empty():  # Check if deque is empty
            print("Deque is empty! Cannot remove from rear.")  # Print error message
        else:
            removed = self.deque.pop()  # Use pop() to remove rear item
            print(f"Removed {removed} from the rear.")  # Print removed item
    
    def is_empty(self):
        """Check if the deque is empty and return a boolean value."""
        return len(self.deque) == 0  # Returns True if deque is empty, otherwise False
    
    def size(self):
        """Return the number of elements in the deque."""
        return len(self.deque)  # Return length of deque
    
    def display(self):
        """Display the elements of the deque."""
        if self.is_empty():  # Check if deque is empty
            print("Deque is empty.")  # Print message if empty
        else:
            print("Deque contents:", list(self.deque))  # Convert deque to list and print contents

# Menu-driven program
if __name__ == "__main__":
    dq = Deque()  # Create an instance of Deque
    while True:
        # Display menu options
        print("\nDouble-Ended Queue Operations:")
        print("1. Add to front")
        print("2. Add to rear")
        print("3. Remove from front")
        print("4. Remove from rear")
        print("5. Display deque")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")  # Take user input for menu choice
        
        if choice == "1":  # Option to add item at the front
            item = input("Enter item to add at front: ")  # Get item input from user
            dq.add_front(item)  # Call add_front method
        elif choice == "2":  # Option to add item at the rear
            item = input("Enter item to add at rear: ")  # Get item input from user
            dq.add_rear(item)  # Call add_rear method
        elif choice == "3":  # Option to remove item from the front
            dq.remove_front()  # Call remove_front method
        elif choice == "4":  # Option to remove item from the rear
            dq.remove_rear()  # Call remove_rear method
        elif choice == "5":  # Option to display the deque
            dq.display()  # Call display method
        elif choice == "6":  # Option to exit the program
            print("Exiting program...")  # Print exit message
            break  # Exit the loop
        else:
            print("Invalid choice! Please enter a number between 1 and 6.")  # Handle invalid input