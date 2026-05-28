PORT_INFO = {
    21: {
        "service": "FTP",
        "purpose": "File transfer service",
        "threat": "Anonymous access exploitation",
        "recommendation": "Disable if unused or secure with authentication"
    },
    22: {
        "service": "SSH",
        "purpose": "Secure remote access",
        "threat": "Brute-force login attempts",
        "recommendation": "Use strong passwords and key authentication"
    },
    23: {
        "service": "TELNET",
        "purpose": "Remote terminal access",
        "threat": "Unencrypted credential interception",
        "recommendation": "Replace with SSH immediately"
    },
    25: {
        "service": "SMTP",
        "purpose": "Email transfer",
        "threat": "Mail relay abuse",
        "recommendation": "Restrict relay permissions"
    },
    53: {
        "service": "DNS",
        "purpose": "Domain resolution",
        "threat": "DNS spoofing attacks",
        "recommendation": "Restrict external queries"
    },
    80: {
        "service": "HTTP",
        "purpose": "Web traffic",
        "threat": "Unencrypted communication",
        "recommendation": "Redirect traffic to HTTPS"
    },
    110: {
        "service": "POP3",
        "purpose": "Email retrieval",
        "threat": "Credential interception",
        "recommendation": "Use encrypted alternatives"
    },
    443: {
        "service": "HTTPS",
        "purpose": "Secure web traffic",
        "threat": "Certificate misconfiguration",
        "recommendation": "Maintain valid certificates"
    }
}


def analyze_port(port):
    return PORT_INFO.get(port)