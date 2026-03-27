import requests


def check_headers(target):
    results = {}

    url = f"http://{target}"

    try:
        response = requests.get(url, timeout=5)
        headers = response.headers

        security_headers = {
            "X-Frame-Options": headers.get("X-Frame-Options"),
            "Content-Security-Policy": headers.get("Content-Security-Policy"),
            "X-XSS-Protection": headers.get("X-XSS-Protection"),
            "Strict-Transport-Security": headers.get("Strict-Transport-Security"),
            "X-Content-Type-Options": headers.get("X-Content-Type-Options"),
        }

        missing = []

        for key, value in security_headers.items():
            if value is None:
                missing.append(key)

        results["headers"] = security_headers
        results["missing"] = missing

    except Exception as e:
        results["error"] = str(e)

    return results