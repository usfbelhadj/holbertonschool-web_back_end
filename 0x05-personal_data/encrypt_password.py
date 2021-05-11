#!/usr/bin/env python3
"""
Encrypting passwords
"""
import bcrypt
from typing import ByteString


def hash_password(password: str) -> ByteString:
    """
    function that expects one string
    argument name password and returns a salted
    """
    return bcrypt.hashpw(b"password", bcrypt.gensalt())
