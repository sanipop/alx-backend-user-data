#!/usr/bin/env python3
""" Script for UserSession module
"""
from models.base import Base


class UserSession(Base):
    """ class for UserSession class
    """

    def __init__(self, *args: list, **kwargs: dict):
        """ Initializer for UserSession
        """
        super().__init__(*args, **kwargs)
        self.user_id = kwargs.get('user_id')
        self.session_id = kwargs.get('session_id')
