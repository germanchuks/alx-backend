#!/usr/bin/python3
"""Module for LFUCache that inherits from BaseCaching."""

BaseCaching = __import__("base_caching").BaseCaching


class LFUCache(BaseCaching):
    """LFUCache class"""

    def __init__(self):
        """Initializes the cache."""
        super().__init__()
        self.uses = dict()

    def put(self, key, item):
        """Assigns to the dictionary self.cache_data the item value for the
        key `key`."""
        if (key is None or item is None):
            return

        if (len(self.cache_data.keys()) == BaseCaching.MAX_ITEMS
           and key not in self.cache_data.keys()):
            discard_key = min(self.uses, key=self.uses.get)
            del self.cache_data[discard_key]
            del self.uses[discard_key]
            print("DISCARD: {}".format(discard_key))
        if (key in self.cache_data.keys()):
            self.uses[key] += 1
        else:
            self.uses[key] = 1
        self.cache_data[key] = item

    def get(self, key):
        """Returns the value in self.cache_data linked to `key`."""
        if (key is None or key not in self.cache_data.keys()):
            return
        self.uses[key] += 1
        return self.cache_data.get(key)
