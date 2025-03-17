class PriorityQueue:

    def __init__(self):
        """Initialize an empty priority queue using a list."""
        self.queue = []   # List to store elements

    def push(self, priority, item):
        """Insert an item into the priority queue with the given priority."""
        self.queue.append((priority, item))
        self.queue.sort(key=lambda x: x[0])

    '''
    instead of lambda we can write - 

    def get_priority(x):
        return x[0]

    self.queue.sort(key=get_priority)
    '''

    def pop(self):
        """Remove and return the item with the highest priority (lowest priority value)."""
        if not self.is_empty():
            return self.queue.pop(0)[1]  # Remove and return the first item (highest priority)
            # self.queue.pop(0) removes the first element from self.queue.
            # since the queue is always sorted by priority, this element has the lowest priority value (highest priority).
            # .pop(0) returns the entire tuple (priority, item).
            # [1] extracts the second value (the item), which is the actual task.
        return None  # Return None if queue is empty

    def peek(self):
        """Return the item with the highest priority without removing it from the queue."""
        if not self.is_empty():
            return self.queue[0][1]  # Return first item's value
        return None  # Return None if queue is empty

    def is_empty(self):
        """Check if the priority queue is empty."""
        return len(self.queue) == 0  # Return True if queue is empty, else False

    def size(self):
        """Return the number of elements in the priority queue."""
        return len(self.queue)  # Return length of queue
    
if __name__ == "__main__":
    pq = PriorityQueue()  # Create an instance of PriorityQueue
    pq.push(2, "Task 2")  # Add task with priority 2
    pq.push(1, "Task 1")  # Add task with priority 1 (highest priority)
    pq.push(3, "Task 3")  # Add task with priority 3

    print("Peek: ", pq.peek())  # Should print "Task 1" (highest priority)
    print("Pop: ", pq.pop())  # Removes and prints "Task 1"
    print("Pop: ", pq.pop())  # Removes and prints "Task 2"
    print("Is Empty: ", pq.is_empty())  # Should return False
    print("Pop: ", pq.pop())  # Removes and prints "Task 3"
    print("Is Empty: ", pq.is_empty())  # Should return True