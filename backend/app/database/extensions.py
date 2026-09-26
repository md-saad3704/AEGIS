"""
Shared database extensions used by the AEGIS backend.

The SQLAlchemy instance is created here without being immediately bound
to a Flask application. The application factory later initializes it
through ``init_database``.

This application-factory pattern keeps the database layer reusable and
makes isolated test databases possible.
"""

from flask_sqlalchemy import SQLAlchemy


# Shared SQLAlchemy extension used by all AEGIS models and services.
#
# The extension is initialized with a Flask application in
# ``app.database.init.init_database`` rather than during module import.
db = SQLAlchemy()