"""Repository operations for route-intersection relationships."""

from sqlalchemy import asc, select

from app.database import db
from app.models.route_intersection import RouteIntersection


class RouteIntersectionRepository:
    """Provide data-access operations for route-intersection records."""

    @staticmethod
    def get_all() -> list[RouteIntersection]:
        """Return all route-intersection relationships ordered by route and sequence."""

        statement = (
            select(RouteIntersection)
            .order_by(
                asc(RouteIntersection.route_id),
                asc(RouteIntersection.sequence_order),
            )
        )

        return list(
            db.session.execute(statement).scalars().all()
        )

    @staticmethod
    def get_by_id(
        relationship_id: int,
    ) -> RouteIntersection | None:
        """Return a route-intersection relationship by primary key."""

        return db.session.get(
            RouteIntersection,
            relationship_id,
        )

    @staticmethod
    def get_for_route(
        route_id: int,
    ) -> list[RouteIntersection]:
        """Return all intersections belonging to a route in traversal order."""

        statement = (
            select(RouteIntersection)
            .where(RouteIntersection.route_id == route_id)
            .order_by(asc(RouteIntersection.sequence_order))
        )

        return list(
            db.session.execute(statement).scalars().all()
        )

    @staticmethod
    def get_for_intersection(
        intersection_id: int,
    ) -> list[RouteIntersection]:
        """Return all routes containing an intersection."""

        statement = (
            select(RouteIntersection)
            .where(
                RouteIntersection.intersection_id == intersection_id
            )
            .order_by(asc(RouteIntersection.route_id))
        )

        return list(
            db.session.execute(statement).scalars().all()
        )