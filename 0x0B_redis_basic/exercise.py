#!/usr/bin/env python3
"""
Redis basic
"""
import redis
from typing import Union
import uuid


class Cache:
    """
    Cache
    """

    def __init__(self):
        """
        In the __init__ method, store an instance of
        the Redis client as a private variable named _redis
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Create a store method that takes a data argument and returns a string
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
