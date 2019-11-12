import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue(DoublyLinkedList):
    def __init__(self):
        # Why is our DLL a good choice to store our elements? O(1) enqueue and dequeue
        super().__init__()

    def enqueue(self, value):
        self.add_to_tail(value)

    def dequeue(self):
        return self.remove_from_head()

    def len(self):
        return self.length
