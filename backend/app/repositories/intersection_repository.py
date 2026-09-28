"""
Repository operations for Intersection records.

This module provides the persistence layer used by AEGIS services
to retrieve intersection records without coupling higher-level
application logic directly to SQLAlchemy queries.
"""

from sqlalchemy import String, cast, select

from ..database import db
from ..models.intersection import Intersection


class IntersectionRepository:
    """Provide database access methods for intersections."""

    @staticmethod
    def get_all() -> list[Intersection]:
        """Return all intersections ordered by primary key."""

        statement = select(Intersection).order_by(
            Intersection.id.asc()
        )

        return list(
            db.session.execute(statement).scalars().all()
        )

    @staticmethod
    def get_by_id(intersection_id: int) -> Intersection | None:
        """Return an intersection by primary key, if it exists."""

        return db.session.get(Intersection, intersection_id)

    @staticmethod
    def get_by_identifier(identifier: str) -> Intersection | None:
        """Return an intersection by its unique identifier."""

        statement = select(Intersection).where(
            cast(Intersection.identifier, String) == identifier
        )

        return db.session.execute(statement).scalar_one_or_none()
