"""
Given a pointer to the head of a linked list and a specific position, 
determine the data value at that position. Count backwards from the tail node. 
The tail is at postion 0, its parent is at 1 and so on.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def getNode(self, positionFromTail):
        def append(head):
            current = head
            elements = []
            while current:
                elements.append(current.data)
                current = current.next
            
            return elements
        
        current = self.head
        elements = append(current)
        if len(elements) == 0:
            return False
        elif len(elements) == 1:
            return elements[0]
        else:
            return elements[-positionFromTail-1]

if __name__ == "__main__":
    linked_list = LinkedList()

    linked_list.head = Node(4)
    three = Node(3)
    two = Node(2)
    one = Node(1)

    linked_list.head.next = three
    three.next = two
    two.next = one

    print(linked_list.getNode(2))