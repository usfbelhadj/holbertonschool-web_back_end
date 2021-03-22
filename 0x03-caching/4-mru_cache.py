#!/usr/bin/env python3
"""MRUCache module
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRUCache definition:
       MRU algorithm
    """

    def __init__(self):
        """[initialization]
        """
        super().__init__()
        self.l_k = []

    def put(self, key, item):
        """[put]
        Args:
            key ([str]): [key]
            item ([str]): [value to assign]
        """
        if key and item:
            self.cache_data[key] = item
            if key not in self.l_k:
                self.l_k.append(key)
            else:
                self.l_k.append(self.l_k.pop(self.l_k.index(key)))
            if len(self.l_k) > BaseCaching.MAX_ITEMS:
                del_key = self.l_k.pop(-2)
                del self.cache_data[del_key]
                print("DISCARD: {}".format(del_key))

    def get(self, key):
        """ Get an item by key
            Return: value or None
        """
        if key and self.cache_data.get(key):
            self.l_k.append(self.l_k.pop(self.l_k.index(key)))
            return self.cache_data.get(key)
        else:
            return None
