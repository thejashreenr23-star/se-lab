class Node:
    def __init__(self, data):
        self.item = data
        self.next = None
        self.prev = None

class doublyLinkedList:
    def __init__(self):
        self.start_node = None

    def InsertToEmptyList(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
        else:
            print("The list is not empty")

    def InsertToEnd(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            return
        n = self.start_node
        while n.next is not None:
            n = n.next
        new_node = Node(data)
        n.next = new_node
        new_node.prev = n

    def DeleteAtStart(self):
        if self.start_node is None:
            print("The linked list is empty, no elements to delete")
            return
        if self.start_node.next is None:
            self.start_node = None
            return
        self.start_node = self.start_node.next
        self.start_node.prev = None

    def DeleteAtEnd(self):
        if self.start_node is None:
            print("The linked list is empty, no elements to delete")
            return
        if self.start_node.next is None:
            self.start_node = None
            return
        n = self.start_node
        while n.next is not None:
            n = n.next
        n.prev.next = None

    def Display(self):
        if self.start_node is None:
            print("The list is empty")
            return
        else:
            n = self.start_node
            while n is not None:
                print("Element is", n.item)
                n = n.next
        print("\n")

# Testing
NewdoublyLinkedList = doublyLinkedList()
NewdoublyLinkedList.InsertToEmptyList(10)
NewdoublyLinkedList.InsertToEnd(20)
NewdoublyLinkedList.InsertToEnd(30)
NewdoublyLinkedList.InsertToEnd(40)
NewdoublyLinkedList.InsertToEnd(50)
NewdoublyLinkedList.InsertToEnd(60)
NewdoublyLinkedList.Display()

print("Before deleting elements")
NewdoublyLinkedList.DeleteAtStart()
print("Deleting element at beginning")
NewdoublyLinkedList.Display()

NewdoublyLinkedList.DeleteAtEnd()
print("Deleting element at end")
NewdoublyLinkedList.Display()
