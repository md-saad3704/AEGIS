import os


class Config:
    """Base configuration for the AEGIS Flask application."""

    SECRET_KEY = os.getenv(
        "SECRET_KEY",
        "development-only-secret-change-me",
    )

    DATABASE_URL = os.getenv(
        "DATABASE_URL",
        "sqlite:///aegis.db",
    )

    CORS_ORIGINS = os.getenv(
        "CORS_ORIGINS",
        "http://localhost:5173",
    )

    DEBUG = os.getenv("FLASK_DEBUG", "false").lower() == "true"