# Class to represent a Node in the linked list
class Node:
    def __init__(self, data):
        self.data = data  # Store the data value
        self.next = None  # Initialize the next pointer to None

# Class to represent the Singly Linked List
class SinglyLinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the list as None

    # Function to insert a new node at the end
    def insert_at_end(self, data):
        new_node = Node(data)  # Create a new node with the given data
        if self.head is None:  # If the list is empty, make new_node the head
            self.head = new_node
            return
        
        # Otherwise, traverse to the last node
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node  # Link the last node to the new node

    # Function to display the linked list
    def display(self):
        if self.head is None:
            print("Linked List is empty")
            return
        
        temp = self.head  # Start from the head
        while temp:
            print(temp.data, end=" -> ")  # Print data followed by an arrow
            temp = temp.next  # Move to the next node
        print("None")  # Indicate the end of the list

    # Function to delete a node with a specific value
    def delete_node(self, key):
        temp = self.head

        # If the head itself holds the key
        if temp is not None and temp.data == key:
            self.head = temp.next  # Move head to the next node
            temp = None  # Delete the old head
            return

        # Search for the key in the list, keep track of the previous node
        prev = None
        while temp is not None and temp.data != key:
            prev = temp
            temp = temp.next

        # If key was not present
        if temp is None:
            print("Key not found in the list")
            return

        # Unlink the node from the linked list
        prev.next = temp.next
        temp = None

# Function to get user input and perform operations on the linked list
def main():
    linked_list = SinglyLinkedList()  # Create an empty linked list
    
    while True:
        print("\nMenu:")
        print("1. Insert at end")
        print("2. Display")
        print("3. Delete node")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            data = int(input("Enter data to insert: "))
            linked_list.insert_at_end(data)
        elif choice == 2:
            linked_list.display()
        elif choice == 3:
            key = int(input("Enter value to delete: "))
            linked_list.delete_node(key)
        elif choice == 4:
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again")

if __name__ == "__main__":
    main()  # Run the main function
