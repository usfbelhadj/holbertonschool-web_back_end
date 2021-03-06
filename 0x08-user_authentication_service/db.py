#!/usr/bin/env python3
"""
DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from typing import TypeVar
from user import Base, User
from sqlalchemy.exc import *
from sqlalchemy.orm.exc import *


class DB:
    """
    DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance"""
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object"""
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """[add_user]

        method, which has two required string arguments:
        email and hashed_password, and returns a User object
        """
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        """[find_user_by]

        Raises:
            NoResultFound: [when no results are found, or when wrong
            query arguments are passed]
            InvalidRequestError: [when no results are found,
            or when wrong query arguments are passed]

        Returns:
            User: [returns the first row found in the users]
        """
        user = self.__session.query(User).filter_by(**kwargs).first()
        if user is None:
            raise NoResultFound
        if kwargs is None:
            raise InvalidRequestError
        return user

    def update_user(self, user_id: int, **kwargs) -> None:

        """[update_user]

        Raises ValueError:
            If an argument that does not correspond
            to a user attribute is passed

        Returns:
            method that takes as argument a required
            user_id integer and arbitrary keyword arguments,
            and returns None
        """
        user = self.find_user_by(id=user_id)
        for k, v in kwargs.items():
            if not hasattr(user, k):
                raise ValueError
            setattr(user, k, v)
        self._session.commit()
