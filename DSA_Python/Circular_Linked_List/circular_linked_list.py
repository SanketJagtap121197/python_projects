class Node:
    """Class to create a Node with data and a pointer to the next node."""
    def __init__(self, data):
        self.data = data  # Store data in the node
        self.next = None  # Pointer to the next node, initially set to None

class CircularLinkedList:
    """Class to create and manage a Circular Linked List."""
    def __init__(self):
        self.head = None  # Initialize the list as empty

    def insert(self, data):
        """Insert a new node at the end of the circular linked list."""
        new_node = Node(data)  # Create a new node with the given data
        if not self.head:  # If the list is empty
            self.head = new_node  # Set new node as head
            self.head.next = self.head  # Point it to itself to maintain circular structure
        else:
            temp = self.head  # Start from head node
            while temp.next != self.head:  # Traverse to the last node
                temp = temp.next
            temp.next = new_node  # Link last node to new node
            new_node.next = self.head  # Maintain circular link by pointing new node to head

    def display(self):
        """Display the circular linked list."""
        if not self.head:  # Check if list is empty
            print("List is empty")  # Print message if list has no nodes
            return
        temp = self.head  # Start from head node
        while True:
            print(temp.data, end=" -> ")  # Print current node data
            temp = temp.next  # Move to next node
            if temp == self.head:  # Stop when we reach back to head
                break
        print("(Back to head)")  # Indicate the circular nature of the list

    def delete(self, key):
        """Delete a node with the given key from the circular linked list."""
        if not self.head:  # Check if the list is empty
            print("List is empty, deletion not possible.")  # Print message if list has no nodes
            return
        
        temp = self.head  # Start from the head node
        prev = None  # Variable to store previous node reference
        while True:
            if temp.data == key:  # Check if current node has the key
                if temp == self.head:  # If the node to be deleted is the head
                    last = self.head  # Find the last node
                    while last.next != self.head:
                        last = last.next
                    if self.head == self.head.next:  # If only one node exists
                        self.head = None  # Remove the only node
                    else:
                        self.head = self.head.next  # Set new head
                        last.next = self.head  # Maintain circular link
                else:
                    prev.next = temp.next  # Skip the current node
                print(f"Deleted {key} from the list.")  # Confirmation message
                return
            prev = temp  # Move previous pointer to current node
            temp = temp.next  # Move current pointer to next node
            if temp == self.head:  # Stop if we complete one full cycle
                break
        print(f"Element {key} not found in the list.")  # Message if element not found

# User interaction loop
def main():
    cll = CircularLinkedList()  # Create an instance of CircularLinkedList
    while True:
        print("\nCircular Linked List Operations:")  # Display menu
        print("1. Insert")  # Option to insert a node
        print("2. Display")  # Option to display the list
        print("3. Delete")  # Option to delete a node
        print("4. Exit")  # Option to exit the program
        
        choice = int(input("Enter your choice: "))  # Get user choice
        if choice == 1:
            data = int(input("Enter data to insert: "))  # Get data from user
            cll.insert(data)  # Insert data into the list
        elif choice == 2:
            cll.display()  # Display the list
        elif choice == 3:
            key = int(input("Enter element to delete: "))  # Get element to delete
            cll.delete(key)  # Delete the node
        elif choice == 4:
            print("Exiting program.")  # Exit message
            break  # Exit the loop
        else:
            print("Invalid choice, try again.")  # Handle invalid input

if __name__ == "__main__":
    main()  # Run the main function
