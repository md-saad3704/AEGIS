import pytest
from flask import Flask

from app.database import db, init_database
from app.models import EmergencyVehicle

@pytest.fixture
def app():
    app = Flask(__name__)

    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    init_database(app)

    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()