import sqlite3
from pathlib import Path

DB_PATH = Path.home() / ".autocare.db"

_connection = None

def get_connection():
    global _connection
    if _connection is None:
        _connection = sqlite3.connect(DB_PATH)
        _connection.row_factory = sqlite3.Row
    return _connection


def initialize_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        Create TABLE IF NOT EXISTS vehicles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            make TEXT NOT NULL,
            model TEXT NOT NULL,
            year INTEGER NOT NULL,
            vin TEXT,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS services (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            vehicle_id INTEGER NOT NULL,
            service_type TEXT NOT NULL,
            odometer INTEGER NOT NULL,
            notes TEXT,
            service_date TEXT,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (vehicle_id) REFERENCES vehicles(id)
        )
    """)

    conn.commit()
