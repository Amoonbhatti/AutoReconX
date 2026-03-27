import requests


def run_live_check(target):
    results = {}

    urls = [
        f"http://{target}",
        f"https://{target}"
    ]

    for url in urls:
        try:
            response = requests.get(url, timeout=5)

            results[url] = {
                "status_code": response.status_code,
                "server": response.headers.get("Server"),
                "content_length": len(response.text)
            }

        except Exception as e:
            results[url] = {
                "error": str(e)
            }

    return results