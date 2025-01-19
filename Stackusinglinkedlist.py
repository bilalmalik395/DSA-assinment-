# Node class to represent each element in the stack
class Node:
    def _init_(self, value):
        self.value = value
        self.next = None

# Stack class to manage stack operations
class Stack:
    def _init_(self):
        self.top = None  # Points to the top of the stack
        self.size = 0    # Keeps track of the stack size

    # Add an element to the top of the stack
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top  # Point the new node to the current top
        self.top = new_node       # Make the new node the top
        self.size += 1

    # Remove and return the top element
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        popped_node = self.top
        self.top = self.top.next  # Set the top to the next node
        self.size -= 1
        return popped_node.value

    # Return the top element without removing it
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.top.value

    # Check if the stack is empty
    def isEmpty(self):
        return self.size == 0

    # Get the current size of the stack
    def stackSize(self):
        return self.size

    # Display all elements in the stack from top to bottom
    def displayStack(self):
        if self.isEmpty():
            print("Stack is empty")
            return
        current = self.top
        while current:
            print(current.value, end=" ")
            current = current.next
        print()

# Create a stack and test the methods
myStack = Stack()

# Test pushing elements onto the stack
myStack.push('A')
myStack.push('B')
myStack.push('C')

# Display the stack
print("Stack: ", end="")
myStack.displayStack()

# Test pop operation
print("Pop: ", myStack.pop())  # Pop and show top item

# Test peek operation
print("Peek: ", myStack.peek())  # Show top item without removing it

# Check if the stack is empty
print("isEmpty: ", myStack.isEmpty())  # Check if stack is empty

# Show the current size of the stack
print("Size: ", myStack.stackSize())  # Show current stack size

# Display the stack again
print("Stack after pop: ", end="")
myStack.displayStack()

# Test pop the rest of the stack
print("Pop: ", myStack.pop())
print("Pop: ", myStack.pop())

# Check if the stack is empty again
print("isEmpty after pops: ", myStack.isEmpty())  # Should be True now
