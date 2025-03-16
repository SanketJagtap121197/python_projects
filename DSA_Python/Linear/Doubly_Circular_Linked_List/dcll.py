class Node:
    def __init__(self, data):
        """Initialize a new node with data, and set next and prev to None"""
        self.data = data
        self.prev = None  # Pointer to the previous node
        self.next = None  # Pointer to the next node

class DoublyCircularLinkedList:
    def __init__(self):
        """Initialize an empty doubly circular linked list"""
        self.head = None  # Head node of the list

    def insert_at_end(self, data):
        """Inserts a new node at the end of the doubly circular linked list."""
        new_node = Node(data)  # Create a new node
        if not self.head:  # If the list is empty
            self.head = new_node
            self.head.next = self.head  # Point next to itself (circular)
            self.head.prev = self.head  # Point prev to itself (circular)
        else:
            last = self.head.prev  # Get the last node
            last.next = new_node  # Link last node's next to new node
            new_node.prev = last  # Link new node's prev to last node
            new_node.next = self.head  # Circular link to head
            self.head.prev = new_node  # Update head's prev to new node

    def insert_at_beginning(self, data):
        """Inserts a new node at the beginning of the list."""
        self.insert_at_end(data)  # Insert at end first
        self.head = self.head.prev  # Move head to the new first node

    def delete_node(self, key):
        """Deletes a node with the given key from the list."""
        if not self.head:  # If list is empty
            print("List is empty!")
            return

        curr = self.head
        while True:
            if curr.data == key:  # Found the node to delete
                if curr == self.head and curr.next == self.head:  # Only one node in the list
                    self.head = None  # Empty the list
                else:
                    curr.prev.next = curr.next  # Bypass current node
                    curr.next.prev = curr.prev  # Update previous node's next
                    if curr == self.head:  # If head is deleted, move it to next node
                        self.head = curr.next
                print(f"Deleted node with value: {key}")
                return
            curr = curr.next
            if curr == self.head:  # Traversed entire list
                break

        print(f"Node with value {key} not found!")

    def search(self, key):
        """Searches for a node with a given key and returns its position."""
        if not self.head:  # If list is empty
            print("List is empty!")
            return -1
        
        curr = self.head
        pos = 0  # Position counter
        while True:
            if curr.data == key:  # If key found
                print(f"Element {key} found at position {pos}")
                return pos
            curr = curr.next
            pos += 1
            if curr == self.head:  # If reached back to head
                break

        print(f"Element {key} not found!")
        return -1

    def display(self):
        """Displays the doubly circular linked list."""
        if not self.head:  # If list is empty
            print("List is empty!")
            return

        curr = self.head
        print("Doubly Circular Linked List:", end=" ")
        while True:
            print(curr.data, end=" ⇄ ")  # Print current node data
            curr = curr.next  # Move to the next node
            if curr == self.head:  # If we reach back to the head
                break
        print("(Back to Head)")

# Testing the Doubly Circular Linked List
if __name__ == "__main__":
    dcll = DoublyCircularLinkedList()
    dcll.insert_at_end(10)
    dcll.insert_at_end(20)
    dcll.insert_at_end(30)
    dcll.insert_at_beginning(5)

    dcll.display()  # Show the list

    dcll.search(20)  # Search for 20
    dcll.delete_node(10)  # Delete node with value 10
    dcll.display()  # Display list after deletion
