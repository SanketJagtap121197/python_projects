class Stack:
    """A simple Stack implementation in Python"""

    def __init__(self):  
        """Initialize an empty list to represent the stack."""
        self.stack = []

    def size(self):
        """Return the size of the stack."""
        size = len(self.stack)
        print(f'📏 Stack size: {size}')
        return size
        
    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.stack) == 0
    
    def push(self, item):
        """Push (add) an item onto the stack."""
        self.stack.append(item)
        print(f'✅ {item} added to the stack')

    def pop(self):
        """Pop (remove) the top item from the stack and return it."""
        if not self.is_empty():
            popped_item = self.stack.pop()
            print(f'❌ {popped_item} removed from the stack')
            return popped_item
        message = "⚠️ Stack is empty! Nothing to remove."
        print(message)
        return message  # Return message for flexibility

    def peek(self):
        """Return the top item without removing it."""
        if not self.is_empty():
            top_item = self.stack[-1]
            print(f'👀 Top element: {top_item}')
            return top_item
        message = "⚠️ Stack is empty! No top element."
        print(message)
        return message  # Return message for flexibility


# 📌 Menu-driven program for stack operations
element = Stack()

while True:
    print("\n🛠 Stack Operation Menu")
    print("1️⃣  Push an element (Add)")
    print("2️⃣  Pop an element (Delete)")
    print("3️⃣  Peek top element (Look)")
    print("4️⃣  Get stack size (Length)")
    print("5️⃣  Exit")
    
    # Ensure the user enters only valid numbers
    try:  
        choice = int(input("🔹 Enter your choice (1 to 5): "))
    except ValueError:
        print("⚠️ Invalid input! Please enter numbers only.")
        continue

    if choice == 1:
        item = input("🔹 Enter an element to push: ")
        element.push(item)

    elif choice == 2:
        element.pop()  # `pop()` already prints output, so no need for extra print()

    elif choice == 3:
        element.peek()  # `peek()` already prints output

    elif choice == 4:
        element.size()  # `size()` already prints output

    elif choice == 5:
        print("👋 Exiting... Thank you!")
        break

    else:
        print("⚠️ Invalid choice! Please enter a number between 1 to 5.")
