class CircularQueue:
    def __init__(self, size):
        # Initialize queue with given size
        self.size = size
        self.queue = [None] * size  # Create an empty list of fixed size
        self.front = self.rear = -1  # Front and Rear pointers

    def enqueue(self, data):
        # Check if the queue is full
        if (self.rear + 1) % self.size == self.front:
            print("Queue is Full")  # Print message if queue is full
            return
        
        # If queue is empty, set front to 0
        if self.front == -1:
            self.front = 0
        
        # Update rear position in a circular manner
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = data  # Insert the element into the queue
        print(f"Inserted {data}")  # Confirm insertion

    def dequeue(self):
        # Check if the queue is empty
        if self.front == -1:
            print("Queue is Empty")  # Print message if queue is empty
            return None
        
        # Fetch the front element to return
        data = self.queue[self.front]
        self.queue[self.front] = None  # Clear the dequeued position
        
        # If there was only one element, reset queue
        if self.front == self.rear:
            self.front = self.rear = -1  # Reset front and rear
        else:
            # Update front in a circular manner
            self.front = (self.front + 1) % self.size
        
        print(f"Deleted {data}")  # Confirm deletion
        return data

    def display(self):
        # Check if the queue is empty
        if self.front == -1:
            print("Queue is Empty")  # Print message if queue is empty
            return
        
        print("Circular Queue:", end=" ")
        i = self.front
        while True:
            print(self.queue[i], end=" ")  # Print each element in queue
            if i == self.rear:
                break
            i = (i + 1) % self.size  # Move to next element circularly
        print()

# User input to interact with CircularQueue
size = int(input("Enter the size of the Circular Queue: "))  # Get queue size from user
cq = CircularQueue(size)  # Create queue instance with given size

while True:
    # Display menu options
    print("\nOptions:")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")
    
    # Get user choice
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        data = int(input("Enter the element to enqueue: "))  # Get element from user
        cq.enqueue(data)  # Add element to queue
    elif choice == 2:
        cq.dequeue()  # Remove element from queue
    elif choice == 3:
        cq.display()  # Display queue contents
    elif choice == 4:
        print("Exiting...")  # Exit message
        break  # Exit loop
    else:
        print("Invalid choice! Please enter a valid option.")  # Handle invalid input
