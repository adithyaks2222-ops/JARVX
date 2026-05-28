import ipaddress


def validate_ip(target):
    try:
        ipaddress.ip_address(target)
        return True
    except ValueError:
        return False