"""
You’re given the pointer to the head nodes of two linked lists. Compare the data in the nodes of the linked lists to 
check if they are equal. If all data attributes are equal and the lists are the same length, return 1. Otherwise, return 0.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def compare_lists(self, llist2):
        current_llist1 = self.head
        current_llist2 = llist2.head
        
        while current_llist1 and current_llist2:
            if current_llist1.data != current_llist2.data:
                return 0
            current_llist1 = current_llist1.next
            current_llist2 = current_llist2.next
            
        if not (current_llist1 or current_llist2):
            return 1
        return 0

if __name__ == "__main__":
    llist1 = LinkedList()
    llist2 = LinkedList()

    llist1.head = Node(1)
    llist2.head = Node(1)

    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    fifth = Node(5)
    sixth = Node(6)

    llist1.head.next = second
    second.next = third
    third.next = fourth

    llist2.head.next = second
    second.next = fifth
    fifth.next = sixth

    print(llist1.compare_lists(llist2))