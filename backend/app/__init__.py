from flask import Flask

from flask_cors import CORS

from .api.routes import api
from .config.settings import Config
from .database import init_database


def create_app():
    """Create and configure the AEGIS Flask application."""

    app = Flask(__name__)
    app.config.from_object(Config)

    init_database(app)

    # Import all SQLAlchemy models so they are registered with
    # the shared metadata before Flask-Migrate/Alembic inspects it.
    from . import models  # noqa: F401

    CORS(
        app,
        origins=app.config["CORS_ORIGINS"].split(","),
    )

    @app.after_request
    def add_security_headers(response):
        """Apply baseline security headers to API responses."""

        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["Referrer-Policy"] = "no-referrer"

        return response

    app.register_blueprint(api)

    return app