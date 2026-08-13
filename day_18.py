class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def display(self):
        current_node = self.head
        while current_node is not None:
            print(f"{current_node.data} -> ",end="")
            current_node = current_node.next
        print("None")

    def prepend(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def length(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count

    def search(self,value):
        current_node = self.head
        while current_node is not None:
            if current_node.data == value:
                return True
            current_node = current_node.next
        return False

    def delete_at_beginning(self):
        if self.head == None:
            print("No List Available!")
        elif self.head.next == None:
            self.head = self.tail = None
        else:
            self.head = self.head.next

    def delete_node(self,value):
        current_node = self.head
        prev_node = None
        while current_node is not None:
            if self.head.data == value:
                self.delete_at_beginning()
                return
            elif current_node.data == value and current_node.next is None:
                self.delete_at_end()
            elif current_node.data == value:
                prev_node.next = current_node.next
                return
            prev_node = current_node
            current_node = current_node.next

    def delete_at_end(self):
        prev_node = self.head
        if self.head is None:
            print("No List Available!")
            return  
        elif self.head == self.tail:
            self.head = self.tail = None
            return     
        while prev_node.next != self.tail:
            prev_node = prev_node.next
        prev_node.next = None
        self.tail = prev_node


lisst = LinkedList()
lisst.append(10)
lisst.append(20)
lisst.append(30)
lisst.append(40)
lisst.append(50)
lisst.append(60)
lisst.display()
lisst.prepend(5)
lisst.display()
print("Length of linkedlist is: ",lisst.length())
if lisst.search(300):
    print("Node Exist")
else:
    print("Not Available")
lisst.delete_at_beginning()
lisst.display()
lisst.delete_node(20)
lisst.display()
lisst.delete_node(60)
lisst.display()
print(lisst.head.data)
print(lisst.tail.data)
lisst.delete_at_end()
lisst.display()