#!/usr/bin/env python3
"""
Session Auth
"""
from api.v1.auth.auth import Auth
from uuid import uuid4
from models.user import User


class SessionAuth(Auth):
    """
    SessionAuth Class
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """[create_session]

        Generate a Session ID using uuid module and uuid4() like id in Base
        Use this Session ID as key of the dictionary user_id_by_session_id -
        the value for this key must be user_id
        Return the Session ID
        The same user_id can have multiple Session ID - indeed, the user_id is
        the value in the dictionary user_id_by_session_id
        """
        if user_id is None or type(user_id) is not str:
            return None
        Session_ID = str(uuid4())
        self.user_id_by_session_id[Session_ID] = user_id
        return Session_ID

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """[user_id_for_session_id]

        Return None if session_id is None
        Return None if session_id is not a string
        Return the value (the User ID) for the key session_id in the
        dictionary user_id_by_session_id.
        You must use .get() built-in for accessing in a dictionary
        a value based on key
        """
        if session_id is None or type(session_id) is not str:
            return None
        User_ID = self.user_id_by_session_id.get(session_id)
        return User_ID

    def current_user(self, request=None):
        """[summary]

        You must use self.session_cookie(...) and
        self.user_id_for_session_id(...)
        to return the User ID based on the cookie _my_session_id
        By using this User ID, you will be able to retrieve
        a User instance fromthe database - you can use User.get(...)
        for retrieving a User from the database.
        """
        session_id = self.session_cookie(request)
        return User.get(self.user_id_for_session_id(session_id))
