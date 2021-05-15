#!/usr/bin/env python3
"""
Session Auth
"""
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """
    SessionAuth Class
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        if user_id is None and type(user_id) != str:
            return None
        Session_ID = uuid.uuid4()
        self.user_id_by_session_id[Session_ID] = user_id
        return Session_ID
