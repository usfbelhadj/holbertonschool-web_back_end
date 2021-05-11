#!/usr/bin/env python3
"""
Encrypting passwords
"""
import bcrypt
from typing import ByteString


def hash_password(password: str) -> ByteString:
    return bcrypt.hashpw(b"password", bcrypt.gensalt())
