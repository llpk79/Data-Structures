import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue(DoublyLinkedList):
    def __init__(self, limit=None):
        # Why is our DLL a good choice to store our elements? O(1) enqueue and dequeue
        super().__init__()
        self.limit = limit

    def enqueue(self, value):
        # If we exceed the length of limit, dequeue and return.
        if self.limit and self.length > self.limit - 1:
            self.add_to_tail(value)
            return self.dequeue()
        self.add_to_tail(value)

    def dequeue(self):
        return self.remove_from_head()

    def len(self):
        return self.length
