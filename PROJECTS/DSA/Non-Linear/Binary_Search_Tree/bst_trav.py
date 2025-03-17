class BST:  # Define a class for the Binary Search Tree (BST)
    def __init__(self, key):  # Constructor to initialize the node with a key
        self.key = key  # Store the value of the current node
        self.left = None  # Initialize the left child as None
        self.right = None  # Initialize the right child as None

    def insert(self, value):  # Method to insert a new value into the BST
        if value < self.key:  # If the value is smaller, go to the left subtree
            if self.left:  # If the left child exists, recursively insert into the left subtree
                self.left.insert(value)
            else:  # If no left child, create a new node and attach it
                self.left = BST(value)  #   Used to create a new node in the left subtree when inserting a new value into the Binary Search Tree (BST)
                #BST(value) → This creates a new node with value as its key.
                # self.left = → This assigns the newly created node to the left child of the current node (self).
        else:  # If the value is greater or equal, go to the right subtree
            if self.right:  # If the right child exists, recursively insert into the right subtree
                self.right.insert(value)
            else:  # If no right child, create a new node and attach it
                self.right = BST(value)

    def inorder_traversal(self):  # Method for in-order traversal (Left, Root, Right)
        if self.left:  # If there is a left child, traverse the left subtree first
            self.left.inorder_traversal()
        print(self.key, end=" ")  # Print the current node's key (root)
        if self.right:  # If there is a right child, traverse the right subtree
            self.right.inorder_traversal()

# Creating and populating the BST
root = BST(10)  # Create the root node with value 10
root.insert(5)  # Insert 5 into the BST (goes to the left of 10)
root.insert(15)  # Insert 15 into the BST (goes to the right of 10)
root.insert(3)  # Insert 3 (goes to the left of 5)
root.insert(7)  # Insert 7 (goes to the right of 5)

# Printing the tree in sorted order using in-order traversal
root.inorder_traversal()  # Output will be: 3 5 7 10 15

