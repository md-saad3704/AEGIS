"""
Database package for the AEGIS backend.

This package exposes the shared Flask-SQLAlchemy database extension,
Flask-Migrate extension, and the helper used to initialize those
extensions with a Flask application.
"""

from .extensions import db, migrate
from .init import init_database

__all__ = ["db", "migrate", "init_database"]