"""
Tests for the AEGIS repository layer.
"""

from app.database import db
from app.models.emergency_vehicle import EmergencyVehicle
from app.repositories.emergency_vehicle_repository import (
    EmergencyVehicleRepository,
)


def test_emergency_vehicle_repository_get_all(app):
    """Verify that all emergency vehicles can be retrieved."""

    vehicle_one = EmergencyVehicle(
        identifier="AMB-101",
        vehicle_type="AMBULANCE",
    )

    vehicle_two = EmergencyVehicle(
        identifier="FIRE-101",
        vehicle_type="FIRE_ENGINE",
    )

    db.session.add_all([vehicle_one, vehicle_two])
    db.session.commit()

    vehicles = EmergencyVehicleRepository.get_all()

    assert len(vehicles) == 2
    assert vehicles[0].identifier == "AMB-101"
    assert vehicles[1].identifier == "FIRE-101"


def test_emergency_vehicle_repository_get_by_id(app):
    """Verify retrieval by primary key."""

    vehicle = EmergencyVehicle(
        identifier="AMB-102",
        vehicle_type="AMBULANCE",
    )

    db.session.add(vehicle)
    db.session.commit()

    result = EmergencyVehicleRepository.get_by_id(vehicle.id)

    assert result is not None
    assert result.id == vehicle.id
    assert result.identifier == "AMB-102"


def test_emergency_vehicle_repository_get_by_identifier(app):
    """Verify retrieval by vehicle identifier."""

    vehicle = EmergencyVehicle(
        identifier="AMB-103",
        vehicle_type="AMBULANCE",
    )

    db.session.add(vehicle)
    db.session.commit()

    result = EmergencyVehicleRepository.get_by_identifier("AMB-103")

    assert result is not None
    assert result.id == vehicle.id
    assert result.identifier == "AMB-103"


def test_emergency_vehicle_repository_missing_vehicle(app):
    """Verify that missing records return None."""

    result = EmergencyVehicleRepository.get_by_id(999999)

    assert result is None

    result = EmergencyVehicleRepository.get_by_identifier("DOES-NOT-EXIST")

    assert result is None

def test_vehicle_position_repository_get_latest_for_vehicle(app):
    """Verify retrieval of the most recent GPS position."""

    from datetime import datetime, timedelta, timezone

    from app.models.vehicle_position import VehiclePosition
    from app.repositories.vehicle_position_repository import (
        VehiclePositionRepository,
    )

    vehicle = EmergencyVehicle(
        identifier="AMB-201",
        vehicle_type="AMBULANCE",
    )

    db.session.add(vehicle)
    db.session.commit()

    now = datetime.now(timezone.utc)

    older_position = VehiclePosition(
        vehicle_id=vehicle.id,
        latitude=26.8500,
        longitude=80.9500,
        speed=40.0,
        heading=90.0,
        timestamp=now - timedelta(minutes=1),
    )

    latest_position = VehiclePosition(
        vehicle_id=vehicle.id,
        latitude=26.8510,
        longitude=80.9510,
        speed=50.0,
        heading=95.0,
        timestamp=now,
    )

    db.session.add_all([older_position, latest_position])
    db.session.commit()

    result = VehiclePositionRepository.get_latest_for_vehicle(vehicle.id)

    assert result is not None
    assert result.id == latest_position.id
    assert result.latitude == 26.8510
    assert result.longitude == 80.9510


def test_vehicle_position_repository_get_track_for_vehicle(app):
    """Verify that a vehicle GPS track is returned chronologically."""

    from datetime import datetime, timedelta, timezone

    from app.models.vehicle_position import VehiclePosition
    from app.repositories.vehicle_position_repository import (
        VehiclePositionRepository,
    )

    vehicle = EmergencyVehicle(
        identifier="AMB-202",
        vehicle_type="AMBULANCE",
    )

    db.session.add(vehicle)
    db.session.commit()

    now = datetime.now(timezone.utc)

    position_one = VehiclePosition(
        vehicle_id=vehicle.id,
        latitude=26.8500,
        longitude=80.9500,
        speed=40.0,
        heading=90.0,
        timestamp=now,
    )

    position_two = VehiclePosition(
        vehicle_id=vehicle.id,
        latitude=26.8510,
        longitude=80.9510,
        speed=45.0,
        heading=92.0,
        timestamp=now + timedelta(minutes=1),
    )

    position_three = VehiclePosition(
        vehicle_id=vehicle.id,
        latitude=26.8520,
        longitude=80.9520,
        speed=50.0,
        heading=95.0,
        timestamp=now + timedelta(minutes=2),
    )

    db.session.add_all(
        [
            position_three,
            position_one,
            position_two,
        ]
    )
    db.session.commit()

    result = VehiclePositionRepository.get_track_for_vehicle(vehicle.id)

    assert len(result) == 3
    assert result[0].id == position_one.id
    assert result[1].id == position_two.id
    assert result[2].id == position_three.id


def test_vehicle_position_repository_get_by_id(app):
    """Verify retrieval of a GPS position by primary key."""

    from datetime import datetime, timezone

    from app.models.vehicle_position import VehiclePosition
    from app.repositories.vehicle_position_repository import (
        VehiclePositionRepository,
    )

    vehicle = EmergencyVehicle(
        identifier="AMB-203",
        vehicle_type="AMBULANCE",
    )

    db.session.add(vehicle)
    db.session.commit()

    position = VehiclePosition(
        vehicle_id=vehicle.id,
        latitude=26.8530,
        longitude=80.9530,
        speed=55.0,
        heading=100.0,
        timestamp=datetime.now(timezone.utc),
    )

    db.session.add(position)
    db.session.commit()

    result = VehiclePositionRepository.get_by_id(position.id)

    assert result is not None
    assert result.id == position.id
    assert result.vehicle_id == vehicle.id


def test_vehicle_position_repository_missing_position(app):
    """Verify that a missing GPS position returns None."""

    from app.repositories.vehicle_position_repository import (
        VehiclePositionRepository,
    )

    result = VehiclePositionRepository.get_by_id(999999)

    assert result is None

def test_route_repository_get_all(app):
    """Verify retrieval of all routes ordered by primary key."""

    from app.models.route import Route
    from app.repositories.route_repository import RouteRepository

    route_one = Route(
        name="Emergency Route A",
        origin="Hospital A",
        destination="Intersection A",
    )

    route_two = Route(
        name="Emergency Route B",
        origin="Hospital B",
        destination="Intersection B",
    )

    db.session.add_all([route_two, route_one])
    db.session.commit()

    result = RouteRepository.get_all()

    assert len(result) == 2
    assert result[0].id < result[1].id
    assert result[0].id == route_two.id
    assert result[1].id == route_one.id

def test_route_repository_get_by_id(app):
    """Verify retrieval of a route by primary key."""

    from app.models.route import Route
    from app.repositories.route_repository import RouteRepository

    route = Route(
        name="Emergency Route C",
        origin="Hospital C",
        destination="Intersection C",
    )

    db.session.add(route)
    db.session.commit()

    result = RouteRepository.get_by_id(route.id)

    assert result is not None
    assert result.id == route.id
    assert result.name == "Emergency Route C"


def test_route_repository_get_by_status(app):
    """Verify retrieval of routes by lifecycle status."""

    from app.models.route import Route
    from app.repositories.route_repository import RouteRepository

    active_route_one = Route(
        name="Active Route A",
        origin="Hospital A",
        destination="Intersection A",
        status="ACTIVE",
    )

    active_route_two = Route(
        name="Active Route B",
        origin="Hospital B",
        destination="Intersection B",
        status="ACTIVE",
    )

    completed_route = Route(
        name="Completed Route",
        origin="Hospital C",
        destination="Intersection C",
        status="COMPLETED",
    )

    db.session.add_all(
        [
            active_route_one,
            active_route_two,
            completed_route,
        ]
    )
    db.session.commit()

    result = RouteRepository.get_by_status("ACTIVE")

    assert len(result) == 2
    assert result[0].id == active_route_one.id
    assert result[1].id == active_route_two.id
    assert all(route.status == "ACTIVE" for route in result)


def test_route_repository_missing_route(app):
    """Verify that a missing route lookup returns None."""

    from app.repositories.route_repository import RouteRepository

    result = RouteRepository.get_by_id(999999)

    assert result is None

def test_intersection_repository_get_all(app):
    """Verify retrieval of all intersections."""

    from app.models.intersection import Intersection
    from app.repositories.intersection_repository import (
        IntersectionRepository,
    )

    intersection_one = Intersection(
        identifier="INT-001",
        latitude=26.8500,
        longitude=80.9500,
    )

    intersection_two = Intersection(
        identifier="INT-002",
        latitude=26.8510,
        longitude=80.9510,
    )

    db.session.add_all([intersection_two, intersection_one])
    db.session.commit()

    result = IntersectionRepository.get_all()

    assert len(result) == 2
    assert result[0].id < result[1].id
    assert result[0].id == intersection_two.id
    assert result[1].id == intersection_one.id


def test_intersection_repository_get_by_id(app):
    """Verify retrieval of an intersection by primary key."""

    from app.models.intersection import Intersection
    from app.repositories.intersection_repository import (
        IntersectionRepository,
    )

    intersection = Intersection(
        identifier="INT-003",
        latitude=26.8520,
        longitude=80.9520,
    )

    db.session.add(intersection)
    db.session.commit()

    result = IntersectionRepository.get_by_id(intersection.id)

    assert result is not None
    assert result.id == intersection.id
    assert result.identifier == "INT-003"


def test_intersection_repository_get_by_identifier(app):
    """Verify retrieval of an intersection by identifier."""

    from app.models.intersection import Intersection
    from app.repositories.intersection_repository import (
        IntersectionRepository,
    )

    intersection = Intersection(
        identifier="INT-004",
        latitude=26.8530,
        longitude=80.9530,
    )

    db.session.add(intersection)
    db.session.commit()

    result = IntersectionRepository.get_by_identifier("INT-004")

    assert result is not None
    assert result.id == intersection.id
    assert result.identifier == "INT-004"


def test_intersection_repository_missing_intersection(app):
    """Verify missing intersection lookups return None."""

    from app.repositories.intersection_repository import (
        IntersectionRepository,
    )

    result_by_id = IntersectionRepository.get_by_id(999999)
    result_by_identifier = (
        IntersectionRepository.get_by_identifier(
            "INT-NOT-FOUND"
        )
    )

    assert result_by_id is None
    assert result_by_identifier is None
