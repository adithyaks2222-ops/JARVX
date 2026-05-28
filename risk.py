RISK_LEVELS = {
    21: "MEDIUM",   # FTP
    22: "LOW",      # SSH
    23: "HIGH",     # TELNET
    25: "MEDIUM",   # SMTP
    53: "LOW",      # DNS
    80: "MEDIUM",   # HTTP
    110: "MEDIUM",  # POP3
    443: "LOW"      # HTTPS
}


def get_risk(port):
    return RISK_LEVELS.get(port, "UNKNOWN")