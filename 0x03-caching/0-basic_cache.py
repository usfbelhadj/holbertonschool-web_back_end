#!/usr/bin/python3
""" BaseCaching module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        BaseCaching.__init__(self)

    def put(self, key, item):
        """ Add an item in the cache
        """
        try:
            self.cache_data[key] = item
            return self.cache_data
        except NotImplementedError:
            BaseCaching().put(key, item)

    def get(self, key):
        """ Get an item by key
        """
        try:
            return self.cache_data[key]
        except KeyError:
            return None
        except NotImplementedError:
            BaseCaching.get(key)
