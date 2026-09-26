"""
Repository operations for simulated emergency response routes.

This repository isolates route-related database queries from the
application and service layers.
"""

from sqlalchemy import cast, String, select

from app.database import db
from app.models.route import Route


class RouteRepository:
    """Provide database operations for simulated routes."""

    @staticmethod
    def get_all() -> list[Route]:
        """Return all routes ordered by their primary key."""

        statement = select(Route).order_by(Route.id.asc())

        return list(db.session.execute(statement).scalars().all())

    @staticmethod
    def get_by_id(route_id: int) -> Route | None:
        """Return a route by its primary key."""

        return db.session.get(Route, route_id)

    @staticmethod
    def get_by_status(status: str) -> list[Route]:
        """Return all routes matching the requested status."""

        statement = (
            select(Route)
            .where(cast(Route.status, String) == status)
            .order_by(Route.id.asc())
        )

        return list(db.session.execute(statement).scalars().all())