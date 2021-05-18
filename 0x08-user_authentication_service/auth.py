#!/usr/bin/env python3
"""
Auth file
"""

import bcrypt


def _hash_password(password: str) -> bytes:
    """[_hash_password]
    method that takes in a password string arguments and returns bytes
    Args:
        password (str)

    Returns:
        bytes
    """
    return bcrypt.hashpw(b"password", bcrypt.gensalt())
