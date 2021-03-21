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
        if key or item is not None:
            self.cache_data[key] = item

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                dicl = sorted(self.cache_data.keys())
                self.cache_data.pop(dicl[0])
                print("DISCARD: {}".format(dicl[0]))

    def get(self, key):
        """ Get an item by key
            Return: value or None
        """

        if key not in self.cache_data.keys():
            return None
        else:
            return self.cache_data[key]
