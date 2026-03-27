def analyze_findings(results):
    findings = []

    # =========================
    # HEADERS CHECK
    # =========================
    headers_data = results.get("headers_check", {})
    missing_headers = headers_data.get("missing", [])

    for header in missing_headers:
        findings.append(f"[!] Missing Security Header: {header}")

    # =========================
    # SSL CHECK
    # =========================
    ssl_data = results.get("ssl", {})

    if "days_remaining" in ssl_data:
        days = ssl_data["days_remaining"]

        if days < 30:
            findings.append(f"[!] SSL certificate expiring soon ({days} days left)")

    # =========================
    # PORT SCAN
    # =========================
    nmap_data = results.get("nmap", "")

    dangerous_ports = ["21", "23", "25", "3389"]

    for port in dangerous_ports:
        if port in str(nmap_data):
            findings.append(f"[!] Dangerous Port Open: {port}")

    return findings