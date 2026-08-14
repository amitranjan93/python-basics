class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Queue:

    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    def dequeue(self):
        if self.head is None:
            print("No Queue Available!")
            return
        elif self.head == self.tail:
            current_node = self.head
            self.head = self.tail = None
            return current_node.data
        current_node = self.head
        self.head = self.head.next
        return current_node.data

    def peek(self):
        if self.head is None:
            print("No Queue Available!")
            return
        return self.head.data

    def is_empty(self):
        return self.head is None

    def display(self):
        current_node = self.head
        while current_node is not None:
            print(f"{current_node.data}-> ",end="")
            current_node = current_node.next
        print("None")

    

queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)
queue.display()
print(queue.dequeue())
queue.display()
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
queue.display()
