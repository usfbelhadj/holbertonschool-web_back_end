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

    def put(self, key, item):
        """ Add an item in the cache
            and delete the other
            Return: Value
        """
        dicl = []
        t = []
        if key or item is not None:
            self.cache_data[key] = item
            for k, v in self.cache_data.items():
                t = [k, v]
                dicl.append(t)
                if len(dicl) > BaseCaching.MAX_ITEMS:
                    print("DISCARD: {}".format(dicl[0][0]))
                    dicl.pop(0)
                    self.cache_data = dict(dicl)
            return self.cache_data
        else:
            return None

    def get(self, key):
        """ Get an item by key
            Return: value or None
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
