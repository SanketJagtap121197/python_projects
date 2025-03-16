# this is dynamic stack no no need to create is_full function to check stack overflow else we would have to use capacity variable to limit capacity like fixed sized stack which are array based
# python list are dynamic
# this is a menu driven program from user

class Stack :
    
    # initialize an empty list to represent the stack
    # remember to always use __init__ to initialize
    def __init__(self):  
        self.stack = []

    def size(self):
        print(f'size of stack : {len(self.stack)}')
        return len(self.stack)
        
    def is_empty(self):
        return len(self.stack) == 0
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if not self.is_empty():
            popped_item = self.stack.pop()
            print(f'{popped_item} is removed from the stack')
            return popped_item           
        print("stack is empty nothing to remove")
        return None
    
    def peek(self):
        if not self.is_empty():
            print(f'top element is {self.stack[-1]}')
            return self.stack[-1]
        print("empty stack, no top element")
        return None   # Return None explicitly when empty
    
element = Stack()

while True:
    print("\n stack operation menu")
    print("1. push an element (add)")
    print("2. pop an element (delete)")
    print("3. peek top element (look)")
    print("4. get stack size (length)")
    print("5. exit")
    
    # to check user only enters numbers
    try:  
        choice = int(input("enter your choice from (1 to 5) : "))
    except ValueError:
        print("invalid input, use only numbers")
        continue

    if choice == 1:
        item = input("enter an element to push : ")
        element.push(item)
    
    elif choice == 2:
        # print("popped last element")
        element.pop()

    elif choice == 3:
        # print("here is top element")
        element.peek()

    elif choice == 4:
        # print("here is the length of stack")
        element.size()

    elif choice == 5:
        print("Exiting...")
        break

    else:
        print("invalid, enter number between (1 to 5)")