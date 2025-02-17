"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def insert_after(self, value):
        """Wrap the given value in a ListNode and insert it
        after this node. Note that this node could already
        have a next node it is point to."""
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    def insert_before(self, value):
        """Wrap the given value in a ListNode and insert it
        before this node. Note that this node could already
        have a previous node it is point to."""
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    def delete(self):
        """Rearranges this ListNode's previous and next pointers
        accordingly, effectively deleting this ListNode."""
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


class DoublyLinkedList:
    """Our doubly-linked list class. It holds references to
    the list's head and tail nodes.
    """

    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_head(self, value):
        """Wraps the given value in a ListNode and inserts it
        as the new head of the list. Don't forget to handle
        the old head node's previous pointer accordingly."""
        if isinstance(value, ListNode):
            new = value
        else:
            new = ListNode(value)
        if not self.head:
            self.head = new
            self.tail = new
        else:
            new.next = self.head
            self.head.prev = new
            self.head = new
        self.length += 1

    def remove_from_head(self):
        """Removes the List's current head node, making the
        current head's next node the new head of the List.
        Returns the value of the removed Node."""
        if not self.head:
            return
        val = self.head.value
        if self.head is self.tail:
            self.head, self.tail = None, None
            self.length = 0
            return val
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        self.length -= 1
        return val

    def add_to_tail(self, value):
        """Wraps the given value in a ListNode and inserts it
        as the new tail of the list. Don't forget to handle
        the old tail node's next pointer accordingly."""
        if isinstance(value, ListNode):
            new = value
        else:
            new = ListNode(value)
        if not self.tail:
            self.head = new
            self.tail = new
        else:
            new.prev = self.tail
            self.tail.next = new
            self.tail = new
        self.length += 1

    def remove_from_tail(self):
        """Removes the List's current tail node, making the
        current tail's previous node the new tail of the List.
        Returns the value of the removed Node."""
        if not self.tail:
            return
        val = self.tail.value
        if self.tail is self.head:
            self.tail, self.head = None, None
            self.length = 0
            return val
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        self.length -= 1
        return val

    def find(self, value):
        if not self.head:
            return False
        curr = self.head
        while curr.next:
            if curr.value == value:
                return curr
            curr = curr.next
        return False

    def move_to_front(self, node):
        """Removes the input node from its current spot in the
        List and inserts it as the new head node of the List."""
        if self.tail is node:
            self.tail = self.tail.prev
            self.tail.next = None
        node.delete()
        self.length -= 1
        self.add_to_head(node)

    def move_to_end(self, node):
        """Removes the input node from its current spot in the
        List and inserts it as the new tail node of the List."""
        if self.head is node:
            self.head = self.head.next
            self.head.prev = None
        node.delete()
        self.length -= 1
        self.add_to_tail(node)

    def delete(self, node):
        """Removes a node from the list and handles cases where
        the node was the head or the tail"""
        if self.head and self.head.value == node.value:
            if self.head.next:
                self.head = self.head.next
                self.head.prev = None
            else:
                self.head = None
        if self.tail and self.tail.value == node.value:
            if self.tail.prev:
                self.tail = self.tail.prev
                self.tail.next = None
            else:
                self.tail = None
        node.delete()
        self.length -= 1

    def get_max(self):
        """Returns the highest value currently in the list"""
        if not self.head:
            return -1
        max_ = self.head.value
        curr = self.head
        while curr.next:
            curr = curr.next
            if curr.value > max_:
                max_ = curr.value
        return max_
