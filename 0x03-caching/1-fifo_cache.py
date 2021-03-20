#!/usr/bin/env python3
"""FIFOCache module
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache definition:
       FIFO algorithm
    """

    def __init__(self):
        """Initiliaze
        """
        super().__init__()
        self.current_keys = []

    def put(self, key, item):
        """ Add an item in the cache
            and delete the other
            Return: Value
        """
        if key is not None or item is not None:
            self.cache_data[key] = item
            if key not in self.current_keys:
                self.current_keys.append(key)
            if len(self.current_keys) > BaseCaching.MAX_ITEMS:
                discarded_key = self.current_keys.pop(0)
                del self.cache_data[discarded_key]
                print('DISCARD: {}'.format(discarded_key))

    def get(self, key):
        """ Get an item by key
            Return: value or None
        """
        if key not in self.cache_data.keys():
            return None
        else:
            return self.cache_data[key]
