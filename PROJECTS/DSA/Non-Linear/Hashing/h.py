# Simple Hash Table Implementation in Python

class HashTable:
    def __init__(self, size):
        # Initialize the hash table with empty lists (for handling collisions)
        self.size = size
        self.table = [list() for _ in range(size)]
        '''
        [list() for _ in range(size)] is a list comprehension that creates a list with size number of empty lists.
        list() is equivalent to [], so this is the same as [[] for _ in range(size)].
        The _ is a throwaway variable used to loop size times without needing the index.
        Each empty list represents a bucket where key-value pairs will be stored in case of hash collisions.
        This ensures that each bucket is independent, preventing unintended modifications across the table.
        '''

    def _hash_function(self, key):
        # Simple hash function using modulo operator
        # The hash function generates a large integer for the given key
        # We use the modulo operator (%) to ensure that the computed index is within the valid range (0 to size-1)
        return hash(key) % self.size

    def insert(self, key, value):
        # Compute the index using the hash function
        index = self._hash_function(key)
        # This line is responsible for determining where in the hash table a given key should be stored, searched, or deleted.
        # Computes index using self._hash_function(key).
        # Stores the key-value pair at self.table[index].
        # If the key already exists, it updates the value
        '''
        Purpose: This line computes the index where the key-value pair will be stored or searched in the hash table.
        How It Works:
        self._hash_function(key) applies a hash function to the given key, converting it into an integer index.
        The index determines which bucket (list) in self.table will hold the key-value pair.
        Why It’s Important:
        Ensures efficient storage and retrieval of data.
        Helps distribute keys evenly across the table to minimize collisions.
        '''
        
        # Check if the key already exists and update it
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
            '''
            pair[0] → The key stored in the hash table.
            pair[1] → The value associated with that key
            '''
        
        # If the key doesn't exist, append it as a new key-value pair
        self.table[index].append([key, value])

    def search(self, key):
        # Compute the index using the hash function
        index = self._hash_function(key)
        # This line is responsible for determining where in the hash table a given key should be stored, searched, or deleted.
        # Computes index using self._hash_function(key).
        # Searches for the key in self.table[index].
        # Returns the value if the key is found, otherwise returns None.
        
        # Search for the key in the bucket
        for pair in self.table[index]: # Iterate through the bucket
            '''
            self.table is a list of lists, where each list represents a "bucket" that stores multiple key-value pairs (in case of hash collisions).
            index is calculated using the hash function to find the correct bucket.
            pair is a key-value pair stored in the bucket.'''
            if pair[0] == key:
                return pair[1]  # Return the value if key is found
        return None  # Return None if key is not found

    def delete(self, key):
        # Compute the index using the hash function
        index = self._hash_function(key)
        
        # Remove the key-value pair if found
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                return True
        return False  # Return False if key was not found

    def display(self):
        # Print the hash table
        for i, bucket in enumerate(self.table):
            # Buckets are used to handle collisions (when multiple keys map to the same index). Since Python’s hash() function can generate the same index for different keys, each bucket holds multiple key-value pairs in a list.
            print(f"Index {i}: {bucket}")

# User input section
if __name__ == "__main__":
    size = int(input("Enter size of hash table: "))  # User inputs table size
    ht = HashTable(size)
    
    while True:
        print("\nOptions: 1. Insert 2. Search 3. Delete 4. Display 5. Exit")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            key = input("Enter key: ")  # User inputs key
            value = input("Enter value: ")  # User inputs value
            ht.insert(key, value)
        elif choice == 2:
            key = input("Enter key to search: ")
            result = ht.search(key)
            print(f"Value found: {result}" if result else "Key not found")
        elif choice == 3:
            key = input("Enter key to delete: ")
            success = ht.delete(key)
            print("Key deleted" if success else "Key not found")
        elif choice == 4:
            ht.display()
        elif choice == 5:
            break
        else:
            print("Invalid choice! Please try again.")
