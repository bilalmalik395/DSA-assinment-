# Node class to represent each element in the queue
class Node:
    def _init_(self, value):
        self.value = value
        self.next = None

# Queue class to manage queue operations
class Queue:
    def _init_(self):
        self.front = None  # Points to the front of the queue
        self.rear = None   # Points to the rear of the queue
        self.size = 0      # Keeps track of the queue size

    # Add an element to the rear of the queue
    def enqueue(self, element):
        new_node = Node(element)
        if self.rear:  # If the queue is not empty
            self.rear.next = new_node
        self.rear = new_node
        if self.front is None:  # If the queue was empty
            self.front = new_node
        self.size += 1

    # Remove and return the element from the front of the queue
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        dequeued_node = self.front
        self.front = self.front.next
        if self.front is None:  # If the queue becomes empty after dequeue
            self.rear = None
        self.size -= 1
        return dequeued_node.value

    # Return the front element without removing it
    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.front.value

    # Check if the queue is empty
    def isEmpty(self):
        return self.size == 0

    # Return the current size of the queue
    def size(self):
        return self.size

    # Display all elements in the queue from front to rear
    def displayQueue(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        current = self.front
        while current:
            print(current.value, end=" ")
            current = current.next
        print()

# Create a queue and test the methods
myQueue = Queue()

# Test enqueuing elements
myQueue.enqueue('A')
myQueue.enqueue('B')
myQueue.enqueue('C')

# Display the queue
print("Queue: ", end="")
myQueue.displayQueue()

# Test dequeue operation
print("Dequeue: ", myQueue.dequeue())  # Dequeue and show front item

# Test peek operation
print("Peek: ", myQueue.peek())  # Show front item without removing it

# Check if the queue is empty
print("isEmpty: ", myQueue.isEmpty())  # Check if queue is empty

# Show the current size of the queue
print("Size: ", myQueue.size())  # Show current queue size

# Display the queue again
print("Queue after dequeue: ", end="")
myQueue.displayQueue()

# Test dequeue the rest of the queue
print("Dequeue: ", myQueue.dequeue())
print("Dequeue: ", myQueue.dequeue())

# Check if the queue is empty again
print("isEmpty after dequeues: ", myQueue.isEmpty())  # 
