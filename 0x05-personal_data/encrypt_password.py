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
    return bcrypt.checkpw(b"password", hashed_password)
