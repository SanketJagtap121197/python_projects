class BST:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.key:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BST(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BST(value)

# Example: Creating a BST
root = BST(10)
root.insert(5)
root.insert(15)
root.insert(3)
root.insert(7)
