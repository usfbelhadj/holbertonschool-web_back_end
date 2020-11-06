#!/usr/bin/python3
""" BaseCaching module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = None

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item is None:
            pass
        else:
            self.cache_data[key] = item
            return self.cache_data

    def get(self, key):
        """ Get an item by key
        """
        if key not in self.cache_data.keys():
            return None
        else:
            return self.cache_data[key]
