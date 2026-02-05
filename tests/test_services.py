import sqlite3
import pytest
from autocare import services

@pytest.fixture
def test_db(monkeypatch):
    """
    In-memory sqlite DB + patched get_connection
    """

    conn = sqlite3.connect(":memory:")

    conn.execute("""
        CREATE TABLE vehicles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            make TEXT,
            model TEXT,
            year INTEGER,
            vin TEXT
        )
    """)

    conn.execute("""
        CREATE TABLE services (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        vehicle_id INTEGER,
        service_type TEXT,
        odometer INTEGER,
        notes TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    def fake_get_connection():
        return conn

    monkeypatch.setattr(services, "get_connection", fake_get_connection)

    yield conn
    conn.close()

# Vehicle tests

def test_add_and_list_vehicle(test_db):
    services.add_vehicle("Honda", "Odyssey", 2006, "123456789ABCDEFGH")

    rows = services.list_vehicles()

    assert len(rows) == 1
    assert rows[0][1] == "Honda"
    assert rows[0][2] == "Odyssey"
    assert rows[0][3] == 2006
    assert rows[0][4] == "123456789ABCDEFGH"


def test_invalid_year(test_db):
    with pytest.raises(ValueError):
        services.add_vehicle("Honda", "Odyssey", 1700, "123456789ABCDEFGH")


# Service tests

def test_add_and_list_service(test_db):
    # Insert vehicle
    cursor = test_db.cursor()
    cursor.execute(
        "INSERT INTO vehicles (make, model, year, vin) VALUES (?, ?, ?, ?)",
        ("Honda", "Odyssey", 2006, "123456789ABCDEFGH"),
    )
    vehicle_id = cursor.lastrowid
    test_db.commit()

    services.add_service(vehicle_id, "oil change", 138100, "synthetic")

    rows = services.list_services(vehicle_id)

    assert len(rows) == 1
    assert rows[0][1] == "Oil Change"
    assert rows[0][2] == 138100
    assert rows[0][3] == "synthetic"


def test_service_vehicle_missing(test_db):
    with pytest.raises(ValueError):
        services.add_service(999, "oil", 1000, None)


def test_negative_odometer(test_db):
    cursor = test_db.cursor()
    cursor.execute(
        "INSERT INTO vehicles (make, model, year, vin) VALUES (?, ?, ?, ?)",
        ("Toyota", "Camry", 2015, "123456789ABCDEFG"),
    )
    vehicle_id = cursor.lastrowid
    test_db.commit()

    with pytest.raises(ValueError):
        services.add_service(vehicle_id, "oil", -5, None)
