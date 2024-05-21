#!/usr/bin/python3
"""Module for LIFOCache that inherits from BaseCaching."""

from collections import deque

BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    """FIFOCache class"""

    def __init__(self):
        """Initializes the cache with an empty deque."""
        super().__init__()
        self.queue = deque()

    def put(self, key, item):
        """Assigns to the dictionary self.cache_data the item value for the
        key `key`."""
        if key and item:
            if key in self.cache_data:
                self.queue.remove(key)
            elif self.is_full():
                self.evict()
            self.queue.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """Returns the value in self.cache_data linked to `key`."""
        return self.cache_data.get(key, None)

    def is_full(self):
        """Checks if the cache has reached its max capacity."""
        return len(self.cache_data) >= self.MAX_ITEMS

    def evict(self):
        """Discards the last item put in cache, and prints `DISCARD` with the
        key discarded."""
        popped = self.queue.pop()
        del self.cache_data[popped]
        print("DISCARD: " + str(popped))
