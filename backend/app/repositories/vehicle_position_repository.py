"""
Repository operations for emergency vehicle GPS positions.

This repository isolates database queries for the vehicle tracking
history from the simulation and application service layers.
"""

from sqlalchemy import select

from ..database import db
from ..models.vehicle_position import VehiclePosition


class VehiclePositionRepository:
    """Provide database operations for vehicle GPS positions."""

    @staticmethod
    def get_latest_for_vehicle(
        vehicle_id: int,
    ) -> VehiclePosition | None:
        """Return the most recent GPS position for a vehicle."""

        statement = (
            select(VehiclePosition)
            .where(VehiclePosition.vehicle_id == vehicle_id)
            .order_by(VehiclePosition.timestamp.desc())
            .limit(1)
        )

        return db.session.execute(statement).scalar_one_or_none()

    @staticmethod
    def get_track_for_vehicle(
        vehicle_id: int,
    ) -> list[VehiclePosition]:
        """Return the complete GPS track for a vehicle in time order."""

        statement = (
            select(VehiclePosition)
            .where(VehiclePosition.vehicle_id == vehicle_id)
            .order_by(VehiclePosition.timestamp.asc())
        )

        return list(db.session.execute(statement).scalars().all())

    @staticmethod
    def get_by_id(position_id: int) -> VehiclePosition | None:
        """Return a GPS position by its primary key."""

        return db.session.get(VehiclePosition, position_id)
