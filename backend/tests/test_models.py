from app.database import db
from app.models.emergency_vehicle import EmergencyVehicle
import pytest

def test_emergency_vehicle_creation(app):
    vehicle = EmergencyVehicle(
        identifier="AMB-001",
        vehicle_type="AMBULANCE",
    )

    db.session.add(vehicle)
    db.session.commit()

    assert vehicle.id is not None
    assert vehicle.identifier == "AMB-001"
    assert vehicle.vehicle_type == "AMBULANCE"
    assert vehicle.status == "ACTIVE"
    assert vehicle.created_at is not None
    assert vehicle.updated_at is not None

def test_vehicle_position_creation(app):
    from app.models.vehicle_position import VehiclePosition

    vehicle = EmergencyVehicle(
        identifier="AMB-002",
        vehicle_type="AMBULANCE",
    )

    db.session.add(vehicle)
    db.session.commit()

    position = VehiclePosition(
        vehicle_id=vehicle.id,
        latitude=26.8467,
        longitude=80.9462,
        speed=45.0,
        heading=90.0,
    )

    db.session.add(position)
    db.session.commit()

    assert position.id is not None
    assert position.vehicle_id == vehicle.id
    assert position.latitude == 26.8467
    assert position.longitude == 80.9462
    assert position.speed == 45.0
    assert position.heading == 90.0
    assert position.timestamp is not None
    assert position.vehicle.identifier == "AMB-002"

def test_route_creation(app):
    from app.models.route import Route

    route = Route(
        name="Emergency Corridor 01",
        origin="Hospital A",
        destination="Trauma Center B",
    )

    db.session.add(route)
    db.session.commit()

    assert route.id is not None
    assert route.name == "Emergency Corridor 01"
    assert route.origin == "Hospital A"
    assert route.destination == "Trauma Center B"
    assert route.status == "ACTIVE"
    assert route.created_at is not None
    assert route.updated_at is not None

def test_intersection_creation(app):
    from app.models.intersection import Intersection

    intersection = Intersection(
        identifier="INT-001",
        latitude=26.8467,
        longitude=80.9462,
    )

    db.session.add(intersection)
    db.session.commit()

    assert intersection.id is not None
    assert intersection.identifier == "INT-001"
    assert intersection.latitude == 26.8467
    assert intersection.longitude == 80.9462
    assert intersection.created_at is not None

def test_route_intersection_creation(app):
    from app.models.intersection import Intersection
    from app.models.route import Route
    from app.models.route_intersection import RouteIntersection

    route = Route(
        name="Emergency Corridor 01",
        origin="Hospital A",
        destination="Trauma Center B",
    )

    intersection = Intersection(
        identifier="INT-002",
        latitude=26.8470,
        longitude=80.9468,
    )

    db.session.add_all([route, intersection])
    db.session.commit()

    route_intersection = RouteIntersection(
        route_id=route.id,
        intersection_id=intersection.id,
        sequence=1,
        distance_from_start=500.0,
    )

    db.session.add(route_intersection)
    db.session.commit()

    assert route_intersection.id is not None
    assert route_intersection.route_id == route.id
    assert route_intersection.intersection_id == intersection.id
    assert route_intersection.sequence == 1
    assert route_intersection.distance_from_start == 500.0
    assert route_intersection.route.name == "Emergency Corridor 01"
    assert route_intersection.intersection.identifier == "INT-002"

def test_route_intersection_constraints(app):
    from sqlalchemy.exc import IntegrityError

    from app.models.intersection import Intersection
    from app.models.route import Route
    from app.models.route_intersection import RouteIntersection

    route = Route(
        name="Emergency Corridor 02",
        origin="Hospital C",
        destination="Trauma Center D",
    )

    intersection_one = Intersection(
        identifier="INT-003",
        latitude=26.8480,
        longitude=80.9470,
    )

    intersection_two = Intersection(
        identifier="INT-004",
        latitude=26.8490,
        longitude=80.9480,
    )

    db.session.add_all([route, intersection_one, intersection_two])
    db.session.commit()

    first = RouteIntersection(
        route_id=route.id,
        intersection_id=intersection_one.id,
        sequence=1,
        distance_from_start=500.0,
    )

    db.session.add(first)
    db.session.commit()

    duplicate_sequence = RouteIntersection(
        route_id=route.id,
        intersection_id=intersection_two.id,
        sequence=1,
        distance_from_start=1000.0,
    )

    db.session.add(duplicate_sequence)

    with pytest.raises(IntegrityError):
        db.session.commit()

    db.session.rollback()

    duplicate_intersection = RouteIntersection(
        route_id=route.id,
        intersection_id=intersection_one.id,
        sequence=2,
        distance_from_start=1000.0,
    )

    db.session.add(duplicate_intersection)

    with pytest.raises(IntegrityError):
        db.session.commit()

    db.session.rollback()

def test_traffic_observation_creation(app):
    from app.models.intersection import Intersection
    from app.models.traffic_observation import TrafficObservation

    intersection = Intersection(
        identifier="INT-005",
        latitude=26.8500,
        longitude=80.9490,
    )

    db.session.add(intersection)
    db.session.commit()

    observation = TrafficObservation(
        intersection_id=intersection.id,
        density=0.65,
        vehicle_count=13,
        source="SIMULATION",
    )

    db.session.add(observation)
    db.session.commit()

    assert observation.id is not None
    assert observation.intersection_id == intersection.id
    assert observation.density == 0.65
    assert observation.vehicle_count == 13
    assert observation.source == "SIMULATION"
    assert observation.timestamp is not None
    assert observation.intersection.identifier == "INT-005"

def test_traffic_signal_creation(app):
    from app.models.intersection import Intersection
    from app.models.traffic_signal import TrafficSignal

    intersection = Intersection(
        identifier="INT-006",
        latitude=26.8510,
        longitude=80.9500,
    )

    db.session.add(intersection)
    db.session.commit()

    signal = TrafficSignal(
        intersection_id=intersection.id,
        current_state="RED",
        normal_cycle_seconds=60,
    )

    db.session.add(signal)
    db.session.commit()

    assert signal.id is not None
    assert signal.intersection_id == intersection.id
    assert signal.current_state == "RED"
    assert signal.normal_cycle_seconds == 60
    assert signal.state_since is not None
    assert signal.created_at is not None
    assert signal.intersection.identifier == "INT-006"

def test_signal_priority_decision_creation(app):
    from app.models.emergency_vehicle import EmergencyVehicle
    from app.models.intersection import Intersection
    from app.models.signal_priority_decision import SignalPriorityDecision

    vehicle = EmergencyVehicle(
        identifier="AMB-002",
        vehicle_type="AMBULANCE",
    )

    intersection = Intersection(
        identifier="INT-007",
        latitude=26.8520,
        longitude=80.9510,
    )

    db.session.add_all([vehicle, intersection])
    db.session.commit()

    decision = SignalPriorityDecision(
        vehicle_id=vehicle.id,
        intersection_id=intersection.id,
        requested_state="GREEN",
        reason="EMERGENCY_PRIORITY",
    )

    db.session.add(decision)
    db.session.commit()

    assert decision.id is not None
    assert decision.vehicle_id == vehicle.id
    assert decision.intersection_id == intersection.id
    assert decision.requested_state == "GREEN"
    assert decision.reason == "EMERGENCY_PRIORITY"
    assert decision.created_at is not None
    assert decision.vehicle.identifier == "AMB-002"
    assert decision.intersection.identifier == "INT-007"

def test_eta_prediction_creation(app):
    from datetime import datetime

    from app.models.emergency_vehicle import EmergencyVehicle
    from app.models.eta_prediction import ETAPrediction
    from app.models.intersection import Intersection

    vehicle = EmergencyVehicle(
        identifier="AMB-003",
        vehicle_type="AMBULANCE",
    )

    intersection = Intersection(
        identifier="INT-008",
        latitude=26.8530,
        longitude=80.9520,
    )

    db.session.add_all([vehicle, intersection])
    db.session.commit()

    predicted_arrival = datetime.now()

    prediction = ETAPrediction(
        vehicle_id=vehicle.id,
        intersection_id=intersection.id,
        predicted_arrival_time=predicted_arrival,
        estimated_seconds=120.0,
        source="BASELINE",
    )

    db.session.add(prediction)
    db.session.commit()

    assert prediction.id is not None
    assert prediction.vehicle_id == vehicle.id
    assert prediction.intersection_id == intersection.id
    assert prediction.predicted_arrival_time == predicted_arrival
    assert prediction.estimated_seconds == 120.0
    assert prediction.source == "BASELINE"
    assert prediction.created_at is not None
    assert prediction.vehicle.identifier == "AMB-003"
    assert prediction.intersection.identifier == "INT-008"

def test_green_corridor_creation(app):
    from app.models.emergency_vehicle import EmergencyVehicle
    from app.models.green_corridor import GreenCorridor
    from app.models.route import Route

    vehicle = EmergencyVehicle(
        identifier="AMB-004",
        vehicle_type="AMBULANCE",
    )

    route = Route(
        name="Emergency Corridor 03",
        origin="Hospital E",
        destination="Trauma Center F",
    )

    db.session.add_all([vehicle, route])
    db.session.commit()

    corridor = GreenCorridor(
        vehicle_id=vehicle.id,
        route_id=route.id,
        status="PLANNED",
    )

    db.session.add(corridor)
    db.session.commit()

    assert corridor.id is not None
    assert corridor.vehicle_id == vehicle.id
    assert corridor.route_id == route.id
    assert corridor.status == "PLANNED"
    assert corridor.created_at is not None
    assert corridor.updated_at is not None
    assert corridor.vehicle.identifier == "AMB-004"
    assert corridor.route.name == "Emergency Corridor 03"
