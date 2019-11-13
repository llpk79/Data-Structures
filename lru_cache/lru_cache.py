import sys
sys.path.append('../doubly_linked_list/')
from doubly_linked_list import DoublyLinkedList, ListNode


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.queue = DoublyLinkedList()
        self.memo = dict()
        self.limit = limit

    def get(self, key):
        """
        Retrieves the value associated with the given key. Also
        needs to move the key-value pair to the end of the order
        such that the pair is considered most-recently used.
        Returns the value associated with the key or None if the
        key-value pair doesn't exist in the cache.
        """
        if key not in self.memo:
            return None

        node = self.memo[key]
        self.queue.move_to_end(node)

        return node.value[1]

    def set(self, key, value):
        """
        Adds the given key-value pair to the cache. The newly-
        added pair should be considered the most-recently used
        entry in the cache. If the cache is already at max capacity
        before this entry is added, then the oldest entry in the
        cache needs to be removed to make room. Additionally, in the
        case that the key already exists in the cache, we simply
        want to overwrite the old value associated with the key with
        the newly-specified value.
        """
        if key in self.memo:
            node = self.memo[key]
            node.value = (key, value)
            self.queue.move_to_end(node)
            return

        node = ListNode((key, value))

        self.memo[key] = node
        self.queue.move_to_end(node)
        self.queue.length += 1

        if self.queue.length > self.limit:
            value_ = self.queue.remove_from_head()
            self.memo.pop(value_[0], None)
            self.queue.length -= 1
