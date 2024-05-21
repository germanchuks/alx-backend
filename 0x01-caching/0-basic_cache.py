#!/usr/bin/python3
"""
Module for BaseCaching that inherits from BasicCache.
"""


BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """BasicCache class"""

    def put(self, key, item):
        """Assigns to the dictionary self.cache_data, the item value for
        the key key."""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Returns the value in self.cache_data linked to key."""
        return self.cache_data.get(key, None)
