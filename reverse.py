"""reverse a singly linked list."""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverse_list(node):
    if not node or not node.next:
        return node
    curr = node
    new = curr.next
    curr.next = None
    while new:
        prev = curr
        curr = new
        new = curr.next
        curr.next = prev
    return curr


"""
1 2 3 4 5 6
^
  
    
"""
one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(5)
one.next = two
two.next = three
three.next = four
four.next = five

rev = reverse_list(one)
curr = rev


def printlist(curr):
    while curr:
        print(curr.value)
        curr = curr.next
