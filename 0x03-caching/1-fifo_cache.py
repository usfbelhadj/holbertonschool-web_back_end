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
        """Assigns item value to key in self.cache_data
            Deletes first element in self.cache_data if elements count is bigger
            then MAX_ITEMS
        """
        if key and item:
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first = sorted(self.cache_data.keys())
            self.cache_data.pop(first[0])
            print("DISCARD: {}".format(first[0]))

    def get(self, key):
        """ Get an item by key
            Return: value or None
        """

        if key not in self.cache_data.keys():
            return None
        else:
            return self.cache_data[key]
