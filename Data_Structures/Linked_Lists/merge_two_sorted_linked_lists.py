"""
Given pointers to the heads of two sorted linked lists, merge 
them into a single, sorted linked list. Either head pointer may be 
null meaning that the corresponding list is empty.

Function Description
Complete the mergeLists function in the editor below.

mergeLists has the following parameters:
- SinglyLinkedListNode pointer headA: a reference to the head of a list
- SinglyLinkedListNode pointer headB: a reference to the head of a list

Returns
SinglyLinkedListNode pointer: a reference to the head of the merged list
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def mergeLists(self, head2):
        head1 = self.head
        head2 = head2.head
        if head1.data < head2.data:
            head = head1
            head1 = head1.next
        else:
            head = head2
            head2 = head2.next
        current = head
        
        while head1 and head2:
            if head1.data < head2.data:
                current.next = head1
                head1 = head1.next
            else:
                current.next = head2
                head2 = head2.next
            current = current.next
            
        if head1:
            current.next = head1
        elif head2:
            current.next = head2
        return head

    def printList(self, llist):
        current = self.head
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        
        print(elements)


if __name__ == "__main__":
    llist1 = LinkedList()
    llist2 = LinkedList()

    llist1.head = Node(1)
    llist2.head = Node(1)
    two = Node(2)
    three = Node(3)
    seven = Node(7)

    llist1.head.next = three
    three.next = seven

    llist2.head.next = two

    result_list = llist1.mergeLists(llist2)
    result_list.printList()