#!/usr/bin/env python3
"""
BaseCaching module
"""

class BaseCaching():
    """
    BaseCaching defines:
    - Content contents of your caching system
    - Where the data are sorted in (a dictionary)
    """
    MAX_ITEMS = 4

    def __int__(self):
        """
        initialize
        """
        self.cache_data = {}


    def print_cache(self):
        """
        Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))


    def put(self, key, item):
        """
        Add an item to the cache
        """
        raise NotImplementedError("Put must be implemented in your cache class")

    
    def get(self, key):
        """
        Get item by key
        """
        raise NotImplementedError("get must be implemented in cache class")
