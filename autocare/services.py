import datetime
from autocare.db import get_connection


def _validate_vehicle_inputs(make, model, year, vin):
    """
    Validates all input and rejects if:
    - make and model does not exist
    - year is not within reasonable bounds
    - VIN length is not 17 or is not uppercase
    - VIN length does not exist or is not alphanumeric
    """
    if not make.strip():
        raise ValueError("Make is required")

    if not model.strip():
        raise ValueError("Model is required")

    current_year = datetime.date.today().year
    if year < 1886 or year > current_year:
        raise ValueError("Year is not valid")

    if not vin or len(vin) != 17 or not vin.isalnum():
        raise ValueError("VIN must be exactly 17 alphanumeric characters")


def _validate_service_inputs(vehicle_id, service_type, odometer):
    """
    Validates all inputs and rejects if:
    - vehicle_id is not an integer or is empty
    - service_type is empty
    - odometer is not an integer OR negative
    """
    if not isinstance(vehicle_id, int):
        raise ValueError("vehicle_id must be an integer")

    if vehicle_id is None:
        raise ValueError("vehicle_id is required")

    if not service_type or not isinstance(service_type, str):
        raise ValueError("service_type is required")

    if odometer is not None:
        if not isinstance(odometer, int):
            raise ValueError("odometer must be an integer")
        if odometer < 0:
            raise ValueError("odometer cannot be negative")


def _validate_odometer_progression(conn, vehicle_id, odometer):
    """
    Validates odometer input so the user is warned if the service
    being added has an out-of-order odometer reading (old records)
    """
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT MAX(odometer)
        FROM services
        WHERE vehicle_id = ?
        """,
        (vehicle_id,)
    )
    row = cursor.fetchone()
    last_odometer = row[0]

    if last_odometer is not None and odometer < last_odometer:
        print(
            f"Warning: odometer ({odometer}) is less than last recorded value "
            f"({last_odometer}). This may be a historical entry."
        )


def _validate_vehicle_exists(conn, vehicle_id):
    cursor = conn.execute(
        "SELECT 1 FROM vehicles WHERE id = ?",
        (vehicle_id,)
    )
    if cursor.fetchone() is None:
        raise ValueError("Vehicle does not exist")


def add_vehicle(make, model, year, vin=None):
    """
    Add a vehicle.
    """

    if vin:
        vin = vin.strip().upper()

    _validate_vehicle_inputs(make, model, year, vin)

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

    _validate_service_inputs(vehicle_id, service_type, odometer)
    _validate_vehicle_exists(conn, vehicle_id)
    _validate_odometer_progression(conn, vehicle_id, odometer)

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
