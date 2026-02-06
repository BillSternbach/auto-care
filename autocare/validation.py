# autocare/validation.py
import datetime

def validate_vehicle_inputs(make, model, year, vin):
    """
    Validate and normalize vehicle inputs.
    Returns normalized VIN.
    """

    if not make or not make.strip():
        raise ValueError("Make is required")

    if not model or not model.strip():
        raise ValueError("Model is required")

    current_year = datetime.date.today().year
    if year < 1886 or year > current_year + 1:
        raise ValueError("Year is not valid")

    if not vin or len(vin) != 17 or not vin.isalnum():
        raise ValueError("VIN must be exactly 17 alphanumeric characters")

    return vin.upper()


def validate_service_inputs(vehicle_id, service_type, odometer):
    """
    Validate basic service inputs.
    """

    if vehicle_id is None or not isinstance(vehicle_id, int):
        raise ValueError("vehicle_id must be an integer")

    if not service_type or not isinstance(service_type, str):
        raise ValueError("service_type is required")

    if odometer is not None:
        if not isinstance (odometer, int):
            raise ValueError("odometer must be an integer")
        if odometer < 0:
            raise ValueError("odometer cannot be negative")


def validate_vehicle_exists(conn, vehicle_id):
    cursor = conn.execute(
        "SELECT 1 FROM vehicles WHERE id = ?",
        (vehicle_id,)
    )
    if cursor.fetchone() is None:
        raise ValueError("Vehicle does not exist")


def validate_odometer_progression(conn, vehicle_id, odometer):
    """
    Warn and not fail if odometer is out of order.
    """
    if odometer is None:
        return

    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT MAX(odometer)
        FROM services
        WHERE vehicle_id = ?
        """,
        (vehicle_id,),
    )
    last_odometer = cursor.fetchone()[0]

    if last_odometer is not None and odometer < last_odometer:
        print(
            f"Warning: odometer ({odometer}) is less than last recorded value "
            f"({last_odometer}). This may be a historical entry."
        )
