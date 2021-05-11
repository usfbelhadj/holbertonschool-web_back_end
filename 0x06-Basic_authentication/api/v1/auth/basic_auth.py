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
        elif type(authorization_header) is not str:
            print("Waht")
            return None
        elif authorization_header[0:6] != "Basic ":
            return None
        else:
            return authorization_header[6:]
