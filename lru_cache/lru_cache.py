import sys
sys.path.append('../queue_and_stack/')
from dll_queue import Queue


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.queue = Queue()
        self.limit = limit
        self.size = 0
        self.memo = dict()

    def move_up(self, key):
        curr = self.queue.head
        while curr.next:
            if curr.value == key:
                break
            curr = curr.next
        self.queue.move_to_end(curr)

    def get(self, key):
        """
        Retrieves the value associated with the given key. Also
        needs to move the key-value pair to the end of the order
        such that the pair is considered most-recently used.
        Returns the value associated with the key or None if the
        key-value pair doesn't exist in the cache.
        """
        if not self.queue or key not in self.memo:
            return None
        self.move_up(key)
        return self.memo[key]

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
            self.memo[key] = value
        else:
            self.memo[key] = value
            self.queue.enqueue(key)
            self.size += 1
            if self.size > self.limit:
                val = self.queue.dequeue()
                self.memo.pop(val, None)
                self.size -= 1
