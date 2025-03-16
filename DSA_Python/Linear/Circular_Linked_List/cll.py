class Node:
    def __init__(self, data):  # Node class to store data and next pointer
        self.data = data  # Store the data value
        self.next = None  # Pointer to the next node, initially None

class CircularLinkedList:
    def __init__(self):  # Initialize the circular linked list
        self.head = None  # Head pointer, initially None

    def append(self, data):  # Method to add a new node at the end
        new_node = Node(data)  # Create a new node
        if not self.head:  # If the list is empty
            self.head = new_node  # Set head to the new node
            self.head.next = self.head  # Point the new node to itself (circular)
        else:
            temp = self.head  # Start from the head
            while temp.next != self.head:  # Traverse to the last node
                temp = temp.next
            temp.next = new_node  # Link last node to the new node
            new_node.next = self.head  # Link new node back to head

    def display(self):  # Method to display the circular linked list
        if not self.head:  # If the list is empty
            print("List is empty")  # Print message
            return  # Exit function
        temp = self.head  # Start from the head
        while True:
            print(temp.data, end=" -> ")  # Print node data
            temp = temp.next  # Move to next node
            if temp == self.head:  # Stop when we reach head again
                break
        print("(Back to head)")  # Indicate circular nature

    def delete(self, key):  # Method to delete a node by value
        if not self.head:  # If the list is empty
            print("List is empty")  # Print message
            return  # Exit function
        
        temp = self.head  # Start from the head
        prev = None  # Previous node pointer, initially None
        
        while True:
            if temp.data == key:  # If node to delete is found
                if prev:  # If deleting a non-head node
                    prev.next = temp.next  # Bypass the node
                else:  # If deleting the head node
                    tail = self.head  # Find the last node (tail)
                    while tail.next != self.head:
                        tail = tail.next
                    if self.head == self.head.next:  # If only one node exists
                        self.head = None  # Set head to None
                    else:
                        tail.next = self.head.next  # Update tail to skip head
                        self.head = self.head.next  # Move head to next node
                print(f"Deleted {key}")  # Print confirmation
                return  # Exit function
            prev = temp  # Move previous pointer
            temp = temp.next  # Move current pointer
            if temp == self.head:  # If we have traversed the whole list
                break
        print(f"{key} not found in the list")  # Print not found message

# Example usage
cll = CircularLinkedList()  # Create circular linked list instance
cll.append(10)  # Add node with data 10
cll.append(20)  # Add node with data 20
cll.append(30)  # Add node with data 30
cll.display()  # Display the list
cll.delete(20)  # Delete node with data 20
cll.display()  # Display the list after deletion