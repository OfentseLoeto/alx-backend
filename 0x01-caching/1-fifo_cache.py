#!/usr/bin/env python3
"""
Define a caching system using first in first out(fifo).
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    Defining a FIFO(FIRST-IN-FIRST-OUT class that inherits
    from its parent class.
    - And is a caching system class
    """
    def __init__(self):
        super().__init__()
        self.queue = []
        self.cache_data = {}

    def put(self, key, item):
        """
        This method mentains a queue to keep track of the order
        in which items were added to the cache.
        -When the number of items exceed the the maximum allowed(
        BaseCaching.MAX_ITEMS), pop the first item from the queue,
        and remove it from the cache.
        -Which implement the FIFO algorithm
        -We then print a message the item is discarded.
        """
        if key is not None and item is not None:
            # Check if cache is full.
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Discard the first item FIFO
                discarded_key = self.queue.pop(0)
                del self.cache_data[discarded_key]
                print(f"DISCARD: {discarded_key}\n")

            self.cache_data[key] = item
            self.queue.append(key)

    def get(self, key):
        """
        This method returns the key for cached data.
        """
        if key is not None:
            return self.cache_data.get(key)
