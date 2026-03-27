import re
import ipaddress


def is_valid_ip(value: str) -> bool:
    try:
        ipaddress.ip_address(value)
        return True
    except ValueError:
        return False


def is_valid_domain(value: str) -> bool:
    domain_regex = re.compile(
        r"^(?!-)[A-Za-z0-9-]{1,63}(?<!-)"
        r"(\.[A-Za-z]{2,})+$"
    )
    return bool(domain_regex.match(value))


def validate_target(target: str) -> bool:
    return is_valid_ip(target) or is_valid_domain(target)