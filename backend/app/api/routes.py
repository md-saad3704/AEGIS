from flask import Blueprint, jsonify


api = Blueprint("api", __name__)


@api.get("/api/health")
def health_check():
    """Return the current health status of the AEGIS API."""

    return jsonify(
        {
            "status": "ok",
            "service": "AEGIS API",
        }
    )