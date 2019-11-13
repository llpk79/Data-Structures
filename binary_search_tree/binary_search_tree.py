import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # Insert the given value into the tree
        if value == self.value:
            return f"Value already in tree"
        if value > self.value:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)

    def contains(self, target):
        # Return True if the tree contains the value
        # False if it does not
        if not self:
            return False
        if self.value == target:
            return True
        if target > self.value:
            if self.right:
                return self.right.contains(target)
            else: return False
        if target < self.value:
            if self.left:
                return self.left.contains(target)
            else: return False

    def get_max(self):
        return self._get_max(self, 0)

    def _get_max(self, node, max_):
        # Return the maximum value found in the tree
        if node.left:
            max_ = self._get_max(node.left, max_)
        if node.right:
            max_ = self._get_max(node.right, max_)
        if node and node.value > max_:
            max_ = node.value
        return max_

    def for_each(self, cb):
        # Call the function `cb` on the value of each node
        # You may use a recursive or iterative approach
        if not self:
            return
        self.value = cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    def in_order_print(self, node):
        # Print all the values in order from low to high
        # Hint:  Use a recursive, depth first traversal
        if not node:
            return
        self.in_order_print(node.left)
        print(node.value)
        self.in_order_print(node.right)

    def bft_print(self, node):
        # Print the value of every node, starting with the given node,
        # in an iterative breadth first traversal
        q = Queue()
        q.enqueue(node)
        ans = ''
        while q:
            curr = q.dequeue()
            if not curr:
                continue
            ans += str(curr.value) + '\n'
            q.enqueue(curr.left)
            q.enqueue(curr.right)
        print(ans[:-1])

    def dft_print(self, node):
        # Print the value of every node, starting with the given node,
        # in an iterative depth first traversal
        stack = Stack()
        stack.push(node)
        ans = ''
        while stack:
            curr = stack.pop()
            if not curr:
                continue
            ans += str(curr.value) + '\n'
            stack.push(curr.left)
            stack.push(curr.right)
        print(ans[:-1])

    # STRETCH Goals -------------------------
    # Note: Research may be required

    def pre_order_dft(self, node):
        # Print In-order recursive DFT
        if not node:
            return
        print(node.value)
        self.pre_order_dft(node.left)
        self.pre_order_dft(node.right)

    def post_order_dft(self, node):
        # Print Post-order recursive DFT
        if not node:
            return
        self.post_order_dft(node.left)
        self.post_order_dft(node.right)
        print(node.value)
