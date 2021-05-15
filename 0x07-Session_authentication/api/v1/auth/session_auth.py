#!/usr/bin/env python3
"""
Session Auth
"""
from api.v1.auth.auth import Auth
from uuid import uuid4


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
