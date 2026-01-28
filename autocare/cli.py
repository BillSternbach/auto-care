import argparse, sys
from autocare.services import (
    add_vehicle,
    list_vehicles,
    add_service,
    list_services,
)


def handle_vehicle_commands(args):
    if args.action == "add":
        add_vehicle(
            make = args.make,
            model = args.model,
            year = args.year,
            vin = args.vin,
        )
        print("Vehicle added.")

    elif args.action == "list":
        vehicles = list_vehicles()
        for v in vehicles:
            print(f"{v['id']}: {v['year']} {v['make']} {v['model']} (VIN: {v['vin']})")

def handle_service_commands(args):
    if args.action == "add":
        try:
            add_service(
                vehicle_id = args.vehicle_id,
                service_type = args.type,
                odometer = args.odometer,
                notes = args.notes,
            )
            print("Service record added.")
        except ValueError as e:
            print(f"Error: {e}")
            sys.exit(1)

    elif args.action == "list":
        services = list_services(args.vehicle_id)
        for s in services:
            print (
                f"{s['id']}: {s['service_type']} "
                f"(Odometer: {s['odometer']}, Notes: {s['notes']}"
            )

def create_parser():
    parser = argparse.ArgumentParser(prog="autocare")

    subparsers = parser.add_subparsers(dest="entity")

    # vehicle commands
    vehicle_parser = subparsers.add_parser("vehicle")
    vehicle_subparsers = vehicle_parser.add_subparsers(dest = "action")

    # autocare vehicle add
    add_parser = vehicle_subparsers.add_parser("add")
    add_parser.add_argument("--make", required=True)
    add_parser.add_argument("--model", required=True)
    add_parser.add_argument("--year", type=int, required=True)
    add_parser.add_argument("--vin")

    # autocare vehicle list
    vehicle_subparsers.add_parser("list")

    # service commands
    service_parser = subparsers.add_parser("service")
    service_subparsers = service_parser.add_subparsers(dest = "action")

    # autocare service add
    service_add = service_subparsers.add_parser("add")
    service_add.add_argument("--vehicle-id", type = int, required = True)
    service_add.add_argument("--type", required = True)
    service_add.add_argument("--odometer", type = int)
    service_add.add_argument("--notes")

    # autocare service list
    service_list = service_subparsers.add_parser("list")
    service_list.add_argument("--vehicle-id", type = int, required = True)

    return parser
