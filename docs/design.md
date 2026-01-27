# Auto Care - Technical Design (MVP)

## Overview
This document describes the technical design for the Auto Care MVP, a CLI-based application for tracking vehicle maintenance records using a local SQLite database.

## CLI Design
The application will be operated via a command line interface using simple functions.

### Supported functions
- autocare vehicle add
- autocare vehicle list
- autocare vehicle add
- autocare vehicle list

## Data Model

### Vehicles Table
Stores vehicle information.

Fields: 
- id (INTEGER, primary key)
- make (TEXT)
- model (TEXT)
- year (INTEGER)
- vin (TEXT, optional)
- created_at (timestamp)

### Services Table
Stores maintenance records.

Fields:
- id (INTEGER, primary key)
- vehicle_id (INTEGER, foreign key to vehicles.id)
- service_type (TEXT)
- odometer (INTEGER)
- notes (TEXT)
- service_date (timestamp)
- created_at (timestamp)

## Project Structure
The project will use a simple and modular python structure.

```text
auto-care/
├── autocare/
│   ├── cli.py
│   ├── db.py
│   ├── models.py
│   └── services.py
├── docs/
│   ├── requiremenets.md
│   └── design.md
├── tests/
├── README.md
└──pyproject.toml
\
```
