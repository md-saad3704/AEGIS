"""
Database package for the AEGIS backend.

This package exposes the shared Flask-SQLAlchemy database extension and
the helper used to initialize that extension with a Flask application.

Keeping database initialization in one place allows the application,
tests, and future services to use the same database abstraction without
coupling domain models to application creation.
"""

from .extensions import db
from .init import init_database

__all__ = ["db", "init_database"]