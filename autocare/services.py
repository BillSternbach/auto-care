from autocare.db import get_connection


def _validate_service_inputs(vehicle_id, service_type, odometer):
    """
    Validates all inputs and rejects if:
    - vehicle_id is not an integer
    - service_type is empty
    - odometer is not an integer OR negative
    """
    if not isinstance(vehicle_id, int):
        raise ValueError("vehicle_id must be an integer")

    if not service_type or not isinstance(service_type, str):
        raise ValueError("service_type must be a non-empty string")

    if odometer is not None:
        if not isinstance(odometer, int):
            raise ValueError("odometer must be an integer")
        if odometer < 0:
            raise ValueError("odometer cannot be negative")


def add_vehicle(make, model, year, vin=None):
    """
    Add a vehicle.
    """
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
    conn.close()


def list_vehicles():
    """
    Lists all vehicles.
    """
    conn = get_connection()
    cursor = conn.cursor()


    cursor.execute("SELECT id, make, model, year, vin FROM vehicles")
    rows = cursor.fetchall()

    conn.close()
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
    _validate_service_inputs(vehicle_id, service_type, odometer)

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO services (vehicle_id, service_type, odometer, notes)
        VALUES (?, ?, ?, ?)
        """,
        (vehicle_id, service_type, odometer, notes),
    )

    conn.commit()
    conn.close()

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
    conn.close()
    return rows
