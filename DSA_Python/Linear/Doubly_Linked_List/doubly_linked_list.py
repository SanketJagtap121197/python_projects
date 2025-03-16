class Node:
    """Class to represent a node in a doubly linked list."""
    def __init__(self, data):
        self.data = data  # Store the data
        self.next = None  # Pointer to the next node
        self.prev = None  # Pointer to the previous node

class DoublyLinkedList:
    """Class to represent the doubly linked list."""
    def __init__(self):
        self.head = None  # Initialize the head of the list
    
    def insert_at_end(self, data):
        """Insert a new node at the end of the list."""
        new_node = Node(data)  # Create a new node with given data
        if self.head is None:  # If the list is empty, make the new node the head
            self.head = new_node
            return
        
        # Traverse to the last node
        temp = self.head
        while temp.next:
            temp = temp.next
        
        temp.next = new_node  # Set last node's next to new node
        new_node.prev = temp  # Set new node's prev to last node
    
    def delete_node(self, key):
        """Delete a node by value (key)."""
        temp = self.head
        
        # If the list is empty
        if temp is None:
            print("List is empty.")
            return
        
        # If head needs to be deleted
        if temp.data == key:
            self.head = temp.next
            if self.head:
                self.head.prev = None
            temp = None  # Free memory
            return
        
        # Search for the node to delete
        while temp and temp.data != key:
            temp = temp.next
        
        if temp is None:  # If the key was not found
            print("Key not found.")
            return
        
        # If the node to be deleted is the last node
        if temp.next:
            temp.next.prev = temp.prev
        
        # If the node to be deleted is in between
        if temp.prev:
            temp.prev.next = temp.next
        
        temp = None  # Free memory
    
    def display_forward(self):
        """Display the list in forward direction."""
        temp = self.head
        while temp:
            print(temp.data, end=' <-> ')
            temp = temp.next
        print("None")
    
    def display_backward(self):
        """Display the list in backward direction."""
        temp = self.head
        if temp is None:
            print("List is empty.")
            return
        
        # Traverse to the last node
        while temp.next:
            temp = temp.next
        
        # Print in reverse order
        while temp:
            print(temp.data, end=' <-> ')
            temp = temp.prev
        print("None")

# Example usage
dll = DoublyLinkedList()

# Allow user to enter elements
n = int(input("Enter the number of elements: "))
for _ in range(n):
    data = int(input("Enter element: "))
    dll.insert_at_end(data)

print("Forward Display:")
dll.display_forward()

print("Backward Display:")
dll.display_backward()

# Allow user to delete an element
delete_key = int(input("Enter the element to delete: "))
dll.delete_node(delete_key)

print("Forward Display after deletion:")
dll.display_forward()
