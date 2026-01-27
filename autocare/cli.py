import argparse
from autocare.services import add_vehicle, list_vehicles


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

def create_parser():
    parser = argparse.ArgumentParser(prog="autocare")

    subparsers = parser.add_subparsers(dest="entity")

    # vehicle commands
    vehicle_parser = subparsers.add_parser("vehicle")
    vehicle_subparsers = vehicle_parser.add_subparsers(dest="action")

    # autocare vehicle add
    add_parser = vehicle_subparsers.add_parser("add")
    add_parser.add_argument("--make", required=True)
    add_parser.add_argument("--model", required=True)
    add_parser.add_argument("--year", type=int, required=True)
    add_parser.add_argument("--vin")

    # autocare vehicle list
    vehicle_subparsers.add_parser("list")

    return parser
