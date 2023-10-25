#!/usr/bin/env python3
"""
Define a caching system class
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    This class inherits BaseCheching class
    - It provides the put and get methods
    - It doesn't have a limit on the number of items
      it can store in the cache
    - It then skip operations if key or item is none
    """
    def __init__(self):
        super().__init__()
        self.cache_data = {}

    def put(self, key, item):
        """
        This method checks if the key or item is none
        - It then assign to the  dictionary the item
          value for the key
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        This function checks if the key is not None

        Args:
            key: They for an item

        Returns:
            Key: Items for the key
        """
        if key is not None:
            return self.cache_data.get(key)
