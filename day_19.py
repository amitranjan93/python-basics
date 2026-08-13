class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node
    def pop(self):
        if self.head is None:
            print("Stack is empty!")
            return None

        current_node = self.head
        self.head = self.head.next
        return current_node.data

    def peek(self):
        if self.head is None:
            print("Stack is Empty!")
        else:
            return self.head.data

    def is_empty(self):
        return self.head is None

    def display(self):
        current_node = self.head
        while current_node is not None:
            print(f"{current_node.data}-> ",end="")
            current_node = current_node.next
        print("None")

new_stack = Stack()
new_stack.push(10)        
new_stack.push(20)        
new_stack.push(30)        
new_stack.push(40)        
new_stack.push(50)        
new_stack.display()
print(f"Popped element is {new_stack.pop()}")
new_stack.display()
print(f"Popped element is {new_stack.pop()}")
new_stack.display()
print(f"Top element is {new_stack.peek()}")
print(f"Stack is empty? {new_stack.is_empty()}")

