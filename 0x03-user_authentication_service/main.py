#!/usr/bin/env python3
"""
for Main Module
"""
from db import DB
from user import User
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound


def register_user(email: str, password: str) -> None:
    """the register_user"""
    assert True
    return


def log_in_wrong_password(email: str, password: str) -> None:
    """module log_in_wrong_password"""
    assert True
    return


def log_in(email: str, password: str) -> str:
    """module log_in"""
    assert True
    return ("")


def profile_unlogged() -> None:
    """the func profile_unlogged"""
    assert True
    return


def profile_logged(session_id: str) -> None:
    """func profile_logged"""
    assert True
    return


def log_out(session_id: str) -> None:
    """the module log_out"""
    assert True
    return


def reset_password_token(email: str) -> str:
    """module func reset_password_token"""
    assert True
    return ("")


def update_password(reset_token: str, new_password: str) -> None:
    """module mess update_password"""
    assert True
    return


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


if __name__ == "__main__":

    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token)
    log_in(EMAIL, NEW_PASSWD)
