from autocare.db import get_connection


def add_vehicle(make, model, year, vin=None):
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
    conn = get_connection()
    cursor = conn.cursor()


    cursor.execute("SELECT id, make, model, year, vin FROM vehicles")
    rows = cursor.fetchall()

    conn.close()
    return rows
