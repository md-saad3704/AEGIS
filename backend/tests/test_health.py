from backend.app import create_app


def test_health_endpoint():
    """Verify that the AEGIS health endpoint responds correctly."""

    app = create_app()
    client = app.test_client()

    response = client.get("/api/health")

    assert response.status_code == 200
    assert response.get_json() == {
        "service": "AEGIS API",
        "status": "ok",
    }


def test_security_headers():
    """Verify baseline security headers are present."""

    app = create_app()
    client = app.test_client()

    response = client.get("/api/health")

    assert response.headers["X-Content-Type-Options"] == "nosniff"
    assert response.headers["X-Frame-Options"] == "DENY"
    assert response.headers["Referrer-Policy"] == "no-referrer"