"""
Database initialization helpers for the AEGIS backend.

Database initialization is kept separate from the Flask application
factory so that the same database setup can be reused by the application,
tests, and future command-line or simulation components.
"""

from flask import Flask

from .extensions import db


def init_database(app: Flask) -> None:
    """
    Initialize the shared SQLAlchemy extension with a Flask application.

    The database URI and SQLAlchemy configuration are expected to already
    be present in the Flask application's configuration before this
    function is called.
    """

    db.init_app(app)