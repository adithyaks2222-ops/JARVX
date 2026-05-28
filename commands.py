def show_help():
    print("""
JARVX SECURITY INTELLIGENCE CORE

Available commands:
  scan <IP>    - Run standard scan
  quick <IP>   - Run quick scan
  deep <IP>    - Run deep scan
  help         - Show help menu
  version      - Show system version
""")


def show_version():
    print("JARVX v1.0 initialized")