# tests/test_services.py
import pytest
from autocare.services import add_service, list_services, add_service, list_services

# Sample in-memory "database" for testing
@pytest.fixture
def empty_records():
    return {"vehicles": {}, "services": {}}

#
# Vehicle Tests
#
def test_add_vehicle(empty_records):
    db = empty_records
    vehicle_data = {"vin": "123ABC", "make": "Honda", "model": "Odyssey", "year": 2006}

    # Add vehicle
    add_vehicle(db, vehicle_data)
    vehicles = list_vehicles(db)

    # Test vehicle was addded
    assert "123ABC" in vehicles
    assert vehicles["123ABC"]["make"] == "Honda"

def test_add_vehicle_duplicate(empty_records):
    db = empty_records
    vehicle_data = {"vin": "123ABC", "make": "Honda", "model": "Odyssey", "year": 2006}

    # Add vehicle twice
    add_vehicle(db, vehicle_data)
    with pytest.raises(ValueError):  # assuming add_vehicle raises ValueError on duplicates
        add_vehicle(db, vehicle_data)

#
# Service tests
#
def test_add_service(empty_records):
    db = empty_records
    vehicle_data = {"vin": "123ABC", "make": "Honda", "model": "Odyssey", "year": 2006}
    add_vehicle(db, vehicle_data)

    # Add a service
    add_service(db, "123ABC", {"service": "Oil change", "odometer": 138100})
    services = list_services(db, "123ABC")

    # Test service was added
    assert services[0]["service"] == "Oil change"
    assert services[0]["odometer"] == 138100

def test_add_service_invalid_vehicle(empty_records):
    db = empty_records
    with pytest.raises(ValueError): # assuming it raises ValueError for non-existent vehicle
        add_service(db, "NONEXISTENT", {"service": "Oil change", "odometer": 1000, "notes": ""})
