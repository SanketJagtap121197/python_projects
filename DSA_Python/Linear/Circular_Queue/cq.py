class CircularQueue:
    def __init__(self, size):
        # Initialize queue with given size
        self.size = size
        self.queue = [None] * size  # Create an empty list of fixed size
        self.front = self.rear = -1  # Front and Rear pointers

    def enqueue(self, data):
        # Check if the queue is full
        if (self.rear + 1) % self.size == self.front:
            print("Queue is Full")
            return
        
        # If queue is empty, set front to 0
        if self.front == -1:
            self.front = 0
        
        # Update rear position in a circular manner
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = data  # Insert the element
        print(f"Inserted {data}")

    def dequeue(self):
        # Check if the queue is empty
        if self.front == -1:
            print("Queue is Empty")
            return None
        
        # Fetch the front element to return
        data = self.queue[self.front]
        self.queue[self.front] = None  # Clear the dequeued position
        
        # If there was only one element, reset queue
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            # Update front in a circular manner
            self.front = (self.front + 1) % self.size
        
        print(f"Deleted {data}")
        return data

    def display(self):
        # Check if the queue is empty
        if self.front == -1:
            print("Queue is Empty")
            return
        
        print("Circular Queue:", end=" ")
        i = self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.size  # Move to next element circularly
        print()

# Testing the CircularQueue implementation
cq = CircularQueue(5)  # Create a queue of size 5
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)
cq.enqueue(50)
cq.display()

cq.dequeue()
cq.dequeue()
cq.display()

cq.enqueue(60)
cq.enqueue(70)
cq.display()
