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
        self.di = []

    def put(self, key, item):
        """ Add an item in the cache
            and delete the other
            Return: Value
        """
        if key and item is not None:
            self.cache_data[key] = item
            if key not in self.di:
                self.di.append(key)
            if len(self.di) > BaseCaching.MAX_ITEMS:
                a = self.di.pop(0)
                self.cache_data.pop(a)
                print("DISCARD: {}".format(a[0]))

    def get(self, key):
        """ Get an item by key
            Return: value or None
        """
        if key not in self.cache_data.keys():
            return None
        else:
            return self.cache_data[key]
