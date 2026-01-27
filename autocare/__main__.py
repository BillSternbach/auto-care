from autocare.db import initialize_db
from autocare.cli import create_parser, handle_vehicle_commands

def main():
    initialize_db()
    parser = create_parser()
    args = parser.parse_args()

    if args.entity == "vehicle":
        handle_vehicle_commands(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
