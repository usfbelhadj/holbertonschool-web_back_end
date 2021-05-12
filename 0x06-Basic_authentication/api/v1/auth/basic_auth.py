#!/usr/bin/env python3
"""
BasicAuth API
"""
from flask import request
from typing import List, TypeVar
from api.v1.auth.auth import Auth
import base64
from typing import TypeVar
from models.user import User


class BasicAuth(Auth):
    """
    BasicAuth Class
    """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
        Basic - Base64 part
        """
        if authorization_header is None:
            return None
        if type(authorization_header) is not str:
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                               str) -> str:
        '''
        returns the decoded value of a Base64 string
        '''

        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) is not str:
            return None
        try:
            base64.b64encode(base64.b64decode(base64_authorization_header
                                              )) == base64_authorization_header
        except Exception:
            return None
        return base64.b64decode(base64_authorization_header).decode('utf-8')

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header:
                                     str) -> (str, str):
        '''
        Basic - User credentials
        '''
        if decoded_base64_authorization_header is None:
            return (None, None)
        if type(decoded_base64_authorization_header) is not str:
            return (None, None)
        if ':' not in decoded_base64_authorization_header:
            return (None, None)
        x, y = decoded_base64_authorization_header.split(':')
        return (x, y)

    def user_object_from_credentials(self, user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        '''
        returns the User instance based on his email and password.
        '''
        if user_email is None or type(user_email) is not str:
            return None
        if user_pwd is None or type(user_pwd) is not str:
            return None
        try:
            users = User.search({'email': user_email})
        except Exception:
            return None
        for user in users:
            if user.is_valid_password(user_pwd):
                return user

        return None
