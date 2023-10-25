0-Create a class FIFOCache that inherits from BaseCaching and is a caching system:

.You must use self.cache_data - dictionary from the parent class BaseCaching
.You can overload def __init__(self): but don’t forget to call the parent init: super().__init__()
.def put(self, key, item):
  >Must assign to the dictionary self.cache_data the item value for the key key.
  >If key or item is None, this method should not do anything.
  >If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:
    -you must discard the first item put in cache (FIFO algorithm)
    -you must print DISCARD: with the key discarded and following by a new line

def get(self, key):
.Must return the value in self.cache_data linked to key.
.If key is None or if the key doesn’t exist in self.cache_data, return None.

1-Create a class LIFOCache that inherits from BaseCaching and is a caching system:

.You must use self.cache_data - dictionary from the parent class BaseCaching
.You can overload def __init__(self): but don’t forget to call the parent init: super().__init__()

def put(self, key, item):
  >Must assign to the dictionary self.cache_data the item value for the key key.
  >If key or item is None, this method should not do anything.
  >If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:
    -you must discard the last item put in cache (LIFO algorithm)
    -you must print DISCARD: with the key discarded and following by a new line

def get(self, key):
.Must return the value in self.cache_data linked to key.
.If key is None or if the key doesn’t exist in self.cache_data, return None.

2-Create a class LIFOCache that inherits from BaseCaching and is a caching system:

.You must use self.cache_data - dictionary from the parent class BaseCaching
.You can overload def __init__(self): but don’t forget to call the parent init: super().__init__()

def put(self, key, item):
  >Must assign to the dictionary self.cache_data the item value for the key key.
  >If key or item is None, this method should not do anything.
  >If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:
    -you must discard the last item put in cache (LIFO algorithm)
    -you must print DISCARD: with the key discarded and following by a new line

def get(self, key):
.Must return the value in self.cache_data linked to key.
.If key is None or if the key doesn’t exist in self.cache_data, return None.

3-Create a class LRUCache that inherits from BaseCaching and is a caching system:

.You must use self.cache_data - dictionary from the parent class BaseCaching
.You can overload def __init__(self): but don’t forget to call the parent init: super().__init__()

def put(self, key, item):
 >Must assign to the dictionary self.cache_data the item value for the key key.
 >If key or item is None, this method should not do anything.
 >If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:
   -you must discard the least recently used item (LRU algorithm)
   -you must print DISCARD: with the key discarded and following by a new line
def get(self, key):
.Must return the value in self.cache_data linked to key.
.If key is None or if the key doesn’t exist in self.cache_data, return None.

4-Create a class MRUCache that inherits from BaseCaching and is a caching system:

.You must use self.cache_data - dictionary from the parent class BaseCaching
.You can overload def __init__(self): but don’t forget to call the parent init: super().__init__()

def put(self, key, item):
>Must assign to the dictionary self.cache_data the item value for the key key.
>If key or item is None, this method should not do anything.
>If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:
  -you must discard the most recently used item (MRU algorithm)
  -you must print DISCARD: with the key discarded and following by a new line

def get(self, key):
.Must return the value in self.cache_data linked to key.
.If key is None or if the key doesn’t exist in self.cache_data, return None.

