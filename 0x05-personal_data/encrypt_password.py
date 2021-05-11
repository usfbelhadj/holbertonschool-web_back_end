#!/usr/bin/env python3
"""
Encrypting passwords
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    function that expects one string
    argument name password and returns a salted
    """
    return bcrypt.hashpw(b"password", bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    is_valid function that expects 2 arguments
    and returns a boolean
    """
    return bcrypt.checkpw(password.encode("utf-8"), hashed_password)
