"""
Repository operations for emergency vehicles.

This repository isolates SQLAlchemy queries from the application
services that operate on emergency vehicles.
"""

from app.database import db
from app.models.emergency_vehicle import EmergencyVehicle


class EmergencyVehicleRepository:
    """Provide database operations for emergency vehicles."""

    @staticmethod
    def get_all() -> list[EmergencyVehicle]:
        """Return all emergency vehicles ordered by database ID."""

        return EmergencyVehicle.query.order_by(
            EmergencyVehicle.id
        ).all()

    @staticmethod
    def get_by_id(vehicle_id: int) -> EmergencyVehicle | None:
        """Return an emergency vehicle by its primary key."""

        return db.session.get(EmergencyVehicle, vehicle_id)

    @staticmethod
    def get_by_identifier(identifier: str) -> EmergencyVehicle | None:
        """Return an emergency vehicle by its unique identifier."""

        return EmergencyVehicle.query.filter_by(
            identifier=identifier
        ).first()