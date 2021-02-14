class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        current = self.head
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        
        print(elements)

    def insertNodeAtPosition(self, data, position):
        current = self.head
        current_id = 0
        new_node = Node(data)

        if position < 1:
            print("Invalid Position!")
            return

        while current_id < position - 1:
            current = current.next
            current_id += 1
        
        new_node.next = current.next
        current.next = new_node


if __name__ == "__main__":
    # Create Linked List object
    linked_list = LinkedList()

    # Create nodes and assign data
    linked_list.head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    fifth = Node(5)

    # Connect all nodes to each other
    linked_list.head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth

    linked_list.display()

    linked_list.insertNodeAtPosition(7, 3)

    linked_list.display()