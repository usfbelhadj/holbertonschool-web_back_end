#!/usr/bin/env python3
"""
BasicAuth API
"""
from flask import request
from typing import List, TypeVar
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """
    BasicAuth Class
    """

    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """
        Basic - Base64 part
        """
        if authorization_header is None:
            return None
        if type(authorization_header) is not str:
            print("Waht")
            return None
        if authorization_header.startswith("Basic "):
            return None
        return authorization_header[6:]
