#!/usr/bin/env python3
"""
Redis basic
"""
import redis
from typing import Union, Callable, Optional
import uuid
from sys import byteorder


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

    def get(
        self, key: str, fn: Optional[Callable] = None
    ) -> Union[str, bytes, int, float]:
        """data back to the desired format."""
        # default Redis.get in case key does not exist
        data = self._redis.get(key)
        # use callable if one provided
        if fn:
            data = fn(data)
        return data

    def get_str(self, data: bytes) -> str:
        """Convert bytes to str"""
        return data.decode("utf-8")

    def get_int(self, data: bytes) -> int:
        """Convert bytes to int"""
        return int.from_bytes(data, byteorder)
