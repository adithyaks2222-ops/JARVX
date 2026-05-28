import sys
from commands import show_help, show_version
from validator import validate_ip
from scanner import scan_ports, quick_scan, deep_scan


def parse_command():
    if len(sys.argv) < 2:
        show_help()
        return

    command = sys.argv[1].lower()

    if command == "help":
        show_help()

    elif command == "version":
        show_version()

    elif command in ["scan", "quick", "deep"]:

        if len(sys.argv) < 3:
            print("[JARVX ERROR] No target IP provided")
            return

        target = sys.argv[2]

        if validate_ip(target):
            print(f"[JARVX] Target validated: {target}")

            if command == "scan":
                scan_ports(target)

            elif command == "quick":
                quick_scan(target)

            elif command == "deep":
                deep_scan(target)

            

        else:
            print("[JARVX ERROR]")
            print("Invalid target format")

    else:
        print(f"[JARVX ERROR] Unknown command: {command}")
        print("Use: python jarvx.py help")