import socket
from risk import get_risk
from mentor import analyze_port
from score import calculate_score, get_status
from results import render_results

COMMON_PORTS = [21, 22, 23, 25, 53, 80, 110, 443]


def run_scan(target, timeout):
    open_ports = []
    results = []

    print("\n[JARVX SCAN INITIATED]\n")

    for port in COMMON_PORTS:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)

        result = sock.connect_ex((target, port))

        if result == 0:
            open_ports.append(port)

            risk = get_risk(port)
            info = analyze_port(port)

            results.append({
                "port": port,
                "state": "OPEN",
                "service": info["service"],
                "risk": risk
            })

            print(f"\n[JARVX ANALYSIS - PORT {port}]")
            print(f"Service: {info['service']}")
            print(f"Purpose: {info['purpose']}")
            print(f"Threat: {info['threat']}")
            print(f"Recommendation: {info['recommendation']}")

        else:
            info = analyze_port(port)

            results.append({
                "port": port,
                "state": "CLOSED",
                "service": info["service"],
                "risk": "--"
            })

        sock.close()

    render_results(results)

    score = calculate_score(open_ports)
    status = get_status(score)

    print("\n[JARVX SECURITY SCORE]")
    print(f"Security Score: {score}/100")
    print(f"Status: {status}")


def scan_ports(target):
    run_scan(target, 1)


def quick_scan(target):
    print("[JARVX QUICK SCAN MODE]")
    run_scan(target, 0.5)


def deep_scan(target):
    print("[JARVX DEEP SCAN MODE]")
    run_scan(target, 2)