from flask import Flask

from app.database import db, init_database


def test_database_initialization():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    init_database(app)

    with app.app_context():
        db.create_all()

        assert db.engine is not None