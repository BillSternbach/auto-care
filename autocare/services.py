import datetime
from autocare.db import get_connection
from autocare.validation import (
    validate_vehicle_inputs,
    validate_service_inputs,
    validate_vehicle_exists,
    validate_odometer_progression,
)


def add_vehicle(make, model, year, vin=None):
    """
    Add a vehicle.
    """
    vin = validate_vehicle_inputs(make, model, year, vin)

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO vehicles (make, model, year, vin)
        VALUES (?, ?, ?, ?)
        """,
        (make, model, year, vin),
    )

    conn.commit()


def list_vehicles():
    """
    Lists all vehicles.
    """
    conn = get_connection()
    cursor = conn.cursor()


    cursor.execute("SELECT id, make, model, year, vin FROM vehicles")
    rows = cursor.fetchall()

    return rows


def add_service(
    vehicle_id: int,
    service_type: str,
    odometer: int | None,
    notes: str | None,
) -> None:
    """
    Add a maintenance record for a specific vehicle.
    """
    conn = get_connection()

    service_type = service_type.strip().title()

    validate_service_inputs(vehicle_id, service_type, odometer)
    validate_vehicle_exists(conn, vehicle_id)
    validate_odometer_progression(conn, vehicle_id, odometer)

    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO services (vehicle_id, service_type, odometer, notes)
        VALUES (?, ?, ?, ?)
        """,
        (vehicle_id, service_type, odometer, notes),
    )

    conn.commit()

def list_services(vehicle_id):
    """
    List all services for a given vehicle.
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT id, service_type, odometer, notes, created_at
        FROM services
        WHERE vehicle_id = ?
        ORDER BY created_at DESC
        """,
        (vehicle_id,),
    )

    rows = cursor.fetchall()
    return rows
