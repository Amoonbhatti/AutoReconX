import socket

common_subdomains = [
    "www", "mail", "admin", "api", "dev", "test", "staging",
    "beta", "portal", "vpn", "cpanel", "webmail"
]

def find_subdomains(domain):
    found = []

    for sub in common_subdomains:
        full_domain = f"{sub}.{domain}"
        try:
            ip = socket.gethostbyname(full_domain)
            found.append((full_domain, ip))
        except:
            pass

    return found