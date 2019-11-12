import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Stack(DoublyLinkedList):
    # Why is our DLL a good choice to store our elements? O(1) pop, push and peek.
    def __init__(self):
        super().__init__()

    def push(self, value):
        self.add_to_tail(value)

    def pop(self):
        return self.remove_from_tail()

    def peek(self):
        return self.tail.value

    def len(self):
        return self.length
