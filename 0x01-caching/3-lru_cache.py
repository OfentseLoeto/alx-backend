#!/usr/bin/env python3
"""
Defining a caching system using (LRUcache) algorithm.
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    Defining the LRUCache that inherits from its parent class
    BaseCaching.
    -It is a caching system class
    """
    def __init__(self):
        super().__init__()
        self.cache_data = {}
        self.order = []

    def put(self, key, item):
        """
         Add an item to the cache using the LRU (Least Recently Used)
         algorithm.

         If the cache is already full (contains BaseCaching.MAX_ITEMS items),
         the least recently used item will be discarded to make space for
         the new item.

         Args:
             key (str): The key to associate with the item.
             item (str): The item to be cached

        Returns:
             None
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Find the list recently used key (the first key
                # in the order list).
                lru_key = self.order.pop(0)
                print(f"DISCARD: {lru_key}")
                del self.cache_data[lru_key]

            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        if key is not None:
            if key in self.cache_data:
                self.order.append(key)
                self.order.remove(key)
                return self.cache_data[key]

        return None
