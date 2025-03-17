# Class representing a node in the Binary Tree
class Node:
    def __init__(self, key):
        self.key = key  # Store the value of the node
        self.left = None  # Left child is initially set to None
        self.right = None  # Right child is initially set to None

# Binary Tree class
class BinaryTree:
    def __init__(self, root_key):
        self.root = Node(root_key)  # Initialize the tree with a root node

    # Insert a node in a binary tree (using level-order traversal)
    def insert(self, key):
        if not self.root:
            self.root = Node(key)  # If tree is empty, create the root node
            return

        queue = [self.root]  # Use a queue for level-order traversal
        while queue:
            temp = queue.pop(0)  # Remove the front node from the queue

            # If the left child is empty, insert the new node here
            if not temp.left:
                temp.left = Node(key)
                return
            else:
                queue.append(temp.left)  # Otherwise, add left child to queue

            # If the right child is empty, insert the new node here
            if not temp.right:
                temp.right = Node(key)
                return
            else:
                queue.append(temp.right)  # Otherwise, add right child to queue

    # Inorder Traversal (Left, Root, Right)
    def inorder(self, node):
        if node:
            self.inorder(node.left)  # Recursively visit left subtree
            print(node.key, end=" ")  # Print the current node
            self.inorder(node.right)  # Recursively visit right subtree

    # Preorder Traversal (Root, Left, Right)
    def preorder(self, node):
        if node:
            print(node.key, end=" ")  # Print the current node
            self.preorder(node.left)  # Recursively visit left subtree
            self.preorder(node.right)  # Recursively visit right subtree

    # Postorder Traversal (Left, Right, Root)
    def postorder(self, node):
        if node:
            self.postorder(node.left)  # Recursively visit left subtree
            self.postorder(node.right)  # Recursively visit right subtree
            print(node.key, end=" ")  # Print the current node after children

# Driver code
if __name__ == "__main__":
    # Create a binary tree with root node 1
    tree = BinaryTree(1)

    # Insert nodes into the binary tree
    tree.insert(2)
    tree.insert(3)
    tree.insert(4)
    tree.insert(5)
    tree.insert(6)
    tree.insert(7)

    # Perform and print Inorder Traversal (should print: 4 2 5 1 6 3 7)
    print("Inorder Traversal:")
    tree.inorder(tree.root)

    # Perform and print Preorder Traversal (should print: 1 2 4 5 3 6 7)
    print("\nPreorder Traversal:")
    tree.preorder(tree.root)

    # Perform and print Postorder Traversal (should print: 4 5 2 6 7 3 1)
    print("\nPostorder Traversal:")
    tree.postorder(tree.root)
