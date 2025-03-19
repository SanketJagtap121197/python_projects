'''
A heap is a special binary tree that follows these rules:

Complete Binary Tree:
All levels are completely filled except possibly the last level, which is filled from left to right.

Heap Property:
Max Heap: The parent node is always greater than or equal to its children.
(Example: The largest element is at the root.)
Min Heap: The parent node is always smaller than or equal to its children.
(Example: The smallest element is at the root.)

How Heap Works
A heap is usually implemented using an array.
For a node at index i:
Left child is at index 2 * i + 1
Right child is at index 2 * i + 2
Parent is at index (i - 1) // 2
'''

'''
e.g. --->  
Step 1: Given Input Array
Let's assume we have the following unsorted array:
arr = [4, 10, 3, 5, 1] 
We need to build a max heap first.

Step 2: Build Max Heap
We start from the last non-leaf node, which is at index n//2 - 1 (where n = 5).

Index	0	1	2	3	4
Array	4	10	3	5	1

Heapify from Index 1 (10, 5, 1)
The node 10 has children 5 and 1.
10 is already the largest, so no change.

Heapify from Index 0 (4, 10, 3)
The node 4 has children 10 and 3.
10 is larger than 4, so we swap 4 and 10.

After heapifying, the Max Heap becomes: [10, 5, 3, 4, 1]
            4
           / \
         10   3
        / \
       5   1   

Array representation: 
arr = [10, 5, 3, 4, 1]      
'''

# Function to heapify a subtree rooted at index i
def heapify(arr, n, i):
    largest = i  # Assume root is the largest
    left = 2 * i + 1  # Left child index
    right = 2 * i + 2  # Right child index
    
    # Check if left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left
    
    # Check if right child exists and is greater than the largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    # If largest is not root, swap and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap values
        heapify(arr, n, largest)  # Recursively heapify the affected subtree

# Function to perform Heap Sort
def heap_sort(arr):
    n = len(arr)
    
    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap max element with last element
        heapify(arr, i, 0)  # Heapify the reduced heap

# Take user input and sort the array
arr = list(map(int, input("Enter numbers separated by spaces: ").split()))  # Read input
heap_sort(arr)  # Perform Heap Sort
print("Sorted array:", arr)  # Display sorted array
