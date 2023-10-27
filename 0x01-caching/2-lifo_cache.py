#!/usr/bin/env python3
"""
Defining a caching system using the (LIFO)algorithm.
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    The LIFO class that inherits from its parent
    class which the BaseCaching.
    """

    def __init__(self):
        super().__init__()
        self.cache_data = {}

    def put(self, key, item):
        """
        Add an item to the cache using the LIFO(LAST_in_first_out)
        algorithm.

        If the cache is already full(contains BaseCaching.MAX_ITEMS
        items), the last item added will be discarded to make space
        for new item.

        Args:
            key (str): The key associated with the item.
            item (str): Item to be cached.

        Returns:
            None.
        """

        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Find the last key to be removed
                # (The last key added to the cache).
                last_in_key = next(iter(self.cache_data))
                print(f"DISCARD: {last_in_key}")
                del self.cache_data[last_in_key]
            
            self.cache_data[key] = item

    def get(self, key):
        """
        This method returns the key for cached data
        else it return none.
        """
        if key is not None:
            return self_.cache_data.get(key)
        else:
            return None
