import ssl
import socket
from datetime import datetime


def check_ssl(target):
    result = {}

    try:
        ctx = ssl.create_default_context()

        with socket.create_connection((target, 443), timeout=5) as sock:
            with ctx.wrap_socket(sock, server_hostname=target) as ssock:
                cert = ssock.getpeercert()

                subject = dict(x[0] for x in cert['subject'])
                issuer = dict(x[0] for x in cert['issuer'])

                expiry = cert['notAfter']
                expiry_date = datetime.strptime(expiry, "%b %d %H:%M:%S %Y %Z")

                days_left = (expiry_date - datetime.utcnow()).days

                result = {
                    "subject": subject,
                    "issuer": issuer,
                    "expiry_date": expiry,
                    "days_remaining": days_left
                }

    except Exception as e:
        result = {"error": str(e)}

    return result