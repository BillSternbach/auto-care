from autocare.db import get_connection


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


def add_service(vehicle_id, service_type, odometer=None, notes=None):
    """
    Add a maintenance record for a specific vehicle.
    """
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
