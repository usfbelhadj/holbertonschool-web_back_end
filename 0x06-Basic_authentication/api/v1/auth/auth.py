#!/usr/bin/env python3
"""
Auth API
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """
    Auth Class
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        returns False - path and excluded_paths will be used later,
        now, you don’t need to take care of them
        """
        if path is None:
            return True
        if excluded_paths is None or "":
            return True
        if path[-1] != "/":
            path += "/"

        if path in excluded_paths:
            return False
        else:
            return True

    def authorization_header(self, request=None) -> str:
        """
        returns None - request will be the Flask request object
        """
        return None

    def current_user(self, request=None) -> TypeVar("User"):
        """
        returns None - request will be the Flask request object
        """
        return None
