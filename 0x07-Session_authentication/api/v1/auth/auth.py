#!/usr/bin/env python3
"""
Auth API
"""
from flask import request
from typing import List, TypeVar
import os


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
        if request is None:
            return None
        if request.headers.get("Authorization", None) is None:
            return None
        return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar("User"):
        """
        returns None - request will be the Flask request object
        """
        return None

    def session_cookie(self, request=None):
        """[session_cookie]

        Return None if request is None
        Return the value of the cookie named _my_session_id
        from request -the name of the cookie must be defined
        by the environment variable SESSION_NAME
        You must use .get() built-in for accessing the
        cookie in the request cookies dictionary
        You must use the environment variable SESSION_NAME to
        define the name of the cookie used for the Session ID
        """
        if request is None:
            return None
        session_name = os.getenv("SESSION_NAME")
        session_id = request.cookies.get(session_name)
        return session_id
